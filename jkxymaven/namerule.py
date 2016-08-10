# -*- coding: utf-8 -*-

BASE_DIR = 'd:\\pyRegularExpression\\Results\\temp\\'

def utf8(origin_str):
    return unicode(origin_str).encode('UTF-8')

def rule_foldername(subfoldername):
    return subfoldername \
        .replace(utf8(u' '), utf8(u'')) \
        .replace(utf8(u'（'), utf8(u'(')) \
        .replace(utf8(u'）'), utf8(u')')) \
        .replace(utf8(u'——'), utf8(u'_')) \
        .replace(utf8(u'－'), utf8(u'_')) \
        .replace(utf8(u'：'), utf8(u'_')) \
        .replace(utf8(u'、'), utf8(u',')) \
        .decode('UTF-8').encode('gbk')  # must not encode to UTF-8, should be encode to GBK



def obtainsubfoldername(urllessonshare, urllessonname, urllessonurl, moduleseq, modulename):
    j = 1
    subfoldername_list = []
    lesson_url_dict = {}
    module_lesson_dict = {}

    for eachlessonname in urllessonshare:
        lessonname = eachlessonname.xpath(urllessonname)[0]
        lessonurl = eachlessonname.xpath(urllessonurl)[0]

        lesson_url_dict[lessonname] = lessonurl

        subfoldername_elements_list = [BASE_DIR, u'JavaScript课程', moduleseq, u'.', j, u'-', modulename, u'-',
                                       lessonname]  ###
        subfoldername_elements_str = [utf8(x) for x in subfoldername_elements_list]  ###
        subfoldername_joint = ''.join(subfoldername_elements_str)
        subfoldername = rule_foldername(subfoldername_joint)
        subfoldername_list.append(subfoldername)
        j += 1
    module_lesson_dict[modulename] = lesson_url_dict
    # module_lesson_dict.items()
    return subfoldername_list, module_lesson_dict

