# -*-coding:utf8-*-
"""
This .py file is for crawling data from those web sites which does not allow directly crawling but could get the
source code via IE.
"""

from lxml import etree
import os
import re
from namerule import obtainsubfoldername, utf8
import pprint

f = open("D:\\GitHub\\repositories\\Spider\\jkxymaven\\webpage_sourcecode\\1.html", "r")
html = f.read()
# print(html)
f.close()

selector = etree.HTML(html)
# 提取文本

""" Define where you want to crwal in the HTML content
"""
urlsharepart = '//div[@id="wrapper"]/div[@id="pager"]/div[@id="container"]/div[@class="wrap w-1000"]/div[@class="pathstage mar-t30"]'
urlmodulepart = 'div[@class="pathstage-txt"]/h2/text()'
urllessonnamesharepart = 'div[@class="stagebox "]/div[@class="stagewidth lesson-list"]/ul/li/div[@class="lesson-infor"]/h2'
urllessonname = 'a/text()'
urllessonurl = 'a/@href'
urlshare = selector.xpath(urlsharepart)

urllessonshare_list = []
lesson_url_dict = {}
module_lesson_dict = {}



"""
"""
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
    return lesson_url_list_a

d = {}
d_list = {}
videofile = [1]
for eachurlshare in urlshare:
    urlmodule = eachurlshare.xpath(urlmodulepart)[0]
    # urlmodule e.g.: 1. JavaScript 开发前的准备
    # print("urlmodule is %s " % urlmodule)
    if urlmodule[1] in range(10):
        # for equal or large than 10
        moduleseq = urlmodule[0:2]
        modulename = urlmodule[4:]  ###
    else:
        # for less than 10
        moduleseq = urlmodule[0]
        modulename = urlmodule[3:]  ###
    print("modulename is %s " % modulename)
    urllessonshare = eachurlshare.xpath(urllessonnamesharepart)
    lessonname_videofile_list = []
    lessonname_videofile_dict = {}
    i = 0
    # lessonname_seq_list = []
    for eachlessonname in urllessonshare:  # cycle within each module
        lessonname = eachlessonname.xpath(urllessonname)[0]
        # lessonname e.g.: JavaScript语法详解
        print("lessonname is %s " % lessonname)
        lessonurl = eachlessonname.xpath(urllessonurl)[0]
        # lessonurl e.g.: http://www.jikexueyuan.com/course/178.html
        # print("lessonurl is %s " % lessonurl)
        lessonname_videofile_dict[lessonname] = videofile
        print("lessonname_videofile_dict is %s " % lessonname_videofile_dict)
        print("lessonname_videofile_list before is %s " % lessonname_videofile_list)
        lessonname_videofile_list = [lessonname_videofile_dict]
        # try:
        #     lessonname_videofile_list.append(lessonname_videofile_dict)
        # except AttributeError:
        #     lessonname_videofile_list = [lessonname_videofile_dict]
        # lessonname_seq_list.append(lessonname)
        print("lessonname_videofile_list after is %s " % lessonname_videofile_list)
        i += 1
        print(i)
    d[modulename] = lessonname_videofile_list

def a():
    return d

print('===============================================================\n' * 10)
pprint.pprint(d)
"""
{'AJAX': [{u'AJAX \u57fa\u7840': [],  # 7
           u'AJAX \u6587\u4ef6\u4e0a\u4f20': [],
           u'AJAX-\u901a\u7528\u4ee3\u7801\u5c01\u88c5\u4e0e\u5e38\u89c1\u95ee\u9898\u5904\u7406': [],
           u'\u5728 jQuery \u4e2d\u4f7f\u7528 AJAX': [],
           u'\u57fa\u4e8e Node.js \u7684\u540e\u7aef\u5e94\u7528\u7b80\u4ecb': [],
           u'\u8de8\u57df AJAX \u7684\u5b9e\u73b0': []}],
 u'JavaScript \u57fa\u7840\u8bed\u6cd5': None,
 u'JavaScript \u5bf9\u8c61': None,
 u'JavaScript \u5f00\u53d1\u524d\u7684\u51c6\u5907': None,
 u'JavaScript \u6587\u6863\u5bf9\u8c61\u6a21\u578b': None,
 u'JavaScript \u6d4f\u89c8\u5668\u5bf9\u8c61': None,
 u'JavaScript \u8bbe\u8ba1\u6a21\u5f0f': [{u'JavaScript \u8bbe\u8ba1\u6a21\u5f0f\u4e4b\u4e2d\u4ecb\u8005\u6a21\u5f0f': [],  # 8
                                           u'JavaScript \u8bbe\u8ba1\u6a21\u5f0f\u4e4b\u5355\u4f8b\u6a21\u5f0f': [],
                                           u'JavaScript \u8bbe\u8ba1\u6a21\u5f0f\u4e4b\u539f\u578b\u6a21\u5f0f': [],
                                           u'JavaScript \u8bbe\u8ba1\u6a21\u5f0f\u4e4b\u547d\u4ee4\u6a21\u5f0f': [],
                                           u'JavaScript \u8bbe\u8ba1\u6a21\u5f0f\u4e4b\u5916\u89c2\u6a21\u5f0f': [],
                                           u'JavaScript \u8bbe\u8ba1\u6a21\u5f0f\u4e4b\u5de5\u5382\u6a21\u5f0f': [],
                                           u'JavaScript \u8bbe\u8ba1\u6a21\u5f0f\u4e4b\u6a21\u677f\u65b9\u6cd5': [],
                                           u'JavaScript \u8bbe\u8ba1\u6a21\u5f0f\u4e4b\u7b56\u7565\u6a21\u5f0f': [],
                                           u'JavaScript \u8bbe\u8ba1\u6a21\u5f0f\u4e4b\u7ec4\u5408\u6a21\u5f0f': [],
                                           u'JavaScript \u8bbe\u8ba1\u6a21\u5f0f\u4e4b\u804c\u8d23\u94fe\u6a21\u5f0f': [],
                                           u'JavaScript \u8bbe\u8ba1\u6a21\u5f0f\u4e4b\u88c5\u9970\u8005\u6a21\u5f0f': [],
                                           u'JavaScript \u8bbe\u8ba1\u6a21\u5f0f\u4e4b\u89c2\u5bdf\u8005\u6a21\u5f0f': [],
                                           u'JavaScript \u8bbe\u8ba1\u6a21\u5f0f\u4e4b\u8fed\u4ee3\u5668\u6a21\u5f0f': [],
                                           u'JavaScript \u8bbe\u8ba1\u6a21\u5f0f\u4e4b\u9002\u914d\u5668\u6a21\u5f0f': [],
                                           u'JavaScript \u8bbe\u8ba1\u6a21\u5f0f\u7b80\u4ecb': [],
                                           u'Javascript \u8bbe\u8ba1\u6a21\u5f0f\u4e4b\u4ee3\u7406\u6a21\u5f0f': [],
                                           u'Javascript \u8bbe\u8ba1\u6a21\u5f0f\u4e4b\u5efa\u9020\u8005\u6a21\u5f0f': [],
                                           u'Javascript \u8bbe\u8ba1\u6a21\u5f0f\u4e4b\u6784\u9020\u51fd\u6570\u6a21\u5f0f': []}],
 u'JavaScript \u9ad8\u7ea7\u6280\u5de7': [{u'JavaScript \u6a21\u5757\u5316': [],  # 6
                                           u'JavaScript\u591a\u7ebf\u7a0b': [],
                                           u'JavaScript\u5f02\u5e38\u5904\u7406\u548c\u4e8b\u4ef6\u5904\u7406': [],
                                           u'JavaScript\u6570\u636e\u63a8\u9001': [],
                                           u'JavaScript\u9762\u5411\u5207\u9762\u7f16\u7a0b': [],
                                           u'JavaScript\u9ad8\u7ea7\u51fd\u6570': [],
                                           u'JavaScript\u9ad8\u7ea7\u6280\u5de7': [],
                                           u'Javascript\u7011\u5e03\u6d41': []}]}
"""



# print(d)
    # print(d[modulename])

# lesson_url_dict[lessonname] = lessonurl
# print(d)

    # build_dict_list = build_dict(urllessonshare, urllessonname, urllessonurl, modulename)
    # d[modulename] = d[modulename].append(build_dict_list[0])
# print(d)

    # createfolder()
    # lesson_url_list_a = obtain_url()
    # print(lesson_url_list_a)
    # print(lesson_url_list)
    # lesson_url_list.extend(lesson_url_list_a)
    # lesson_url_list.extend(a())
    # import itertools
    # list(itertools.chain.from_iterable(lesson_url_list))

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