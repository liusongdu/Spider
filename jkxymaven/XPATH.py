# -*-coding:utf8-*-
"""
This .py file is for crawling data from those web sites which does not allow directly crawling but could get the
source code via IE.
"""

from lxml import etree
import os
import re
from namerule import obtainsubfoldername

f = open("D:\\GitHub\\repositories\\Spider\\jkxymaven\\HTML_files_source_code\\1.html", "r")
html = f.read()
# print(html)
f.close()

selector = etree.HTML(html)
# 提取文本

urlsharepart = '//div[@id="wrapper"]/div[@id="pager"]/div[@id="container"]/div[@class="wrap w-1000"]/div[@class="pathstage mar-t30"]'
urlmodulepart = 'div[@class="pathstage-txt"]/h2/text()'
urllessonnamesharepart = 'div[@class="stagebox "]/div[@class="stagewidth lesson-list"]/ul/li/div[@class="lesson-infor"]/h2'
urllessonname = 'a/text()'
urllessonurl = 'a/@href'
urlshare = selector.xpath(urlsharepart)

urllessonshare_list = []
lesson_url_dict = {}
module_lesson_dict = {}

def createfolder():
    obtainsubfoldername_dict = obtainsubfoldername(urllessonshare, urllessonname, urllessonurl, moduleseq, modulename)
    subfoldername = obtainsubfoldername_dict[0]
    for folder in subfoldername:
        os.mkdir(folder)

lesson_url_list_a = []
lesson_url_list_b = []
lesson_url_list = []

def obtain_url():
    obtainsubfoldername_dict = obtainsubfoldername(urllessonshare, urllessonname, urllessonurl, moduleseq, modulename)
    for x in obtainsubfoldername_dict[1].items():
        url_list = x[1]
        for y in url_list.items():
            url = y[1]
            lesson_url_list_a.append(url)
        # lesson_url_list_b.extend(lesson_url_list_a)
    # print(lesson_url_list_b)
    return lesson_url_list_a

for eachurlshare in urlshare:
    urlmodule = eachurlshare.xpath(urlmodulepart)[0]
    if urlmodule[1] in range(10):
        # for equal or large than 10
        moduleseq = urlmodule[0:2]
        modulename = urlmodule[4:]  ###
    else:
        # for less than 10
        moduleseq = urlmodule[0]
        modulename = urlmodule[3:]  ###
    urllessonshare = eachurlshare.xpath(urllessonnamesharepart)

    # createfolder()
    lesson_url_list_a = obtain_url()
    # print(lesson_url_list_a)
    # print(lesson_url_list)
    # lesson_url_list.extend(lesson_url_list_a)
    # lesson_url_list.extend(a())
    # import itertools
    # list(itertools.chain.from_iterable(lesson_url_list))

def final_obtain_url():
    print(lesson_url_list_a)
    return lesson_url_list_a

'''
lessonname1 = selector.xpath(urlsharepart + urllessonname1)
for eachlessonname1 in lessonname1:
    print (eachlessonname1)
'''

# module = selector.xpath('//div[@id="wrapper"]/div[@id="pager"]/div[@id="container"]/div[@class="wrap w-1000"]')
# title = .extract().replace(' ', '')

''' 1. Course = Python
    2. Module
    3. Lesson
'''

# if __name__ == "__main__":
#     createfolder()