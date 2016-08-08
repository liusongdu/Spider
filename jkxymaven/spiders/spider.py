# -*- coding: utf-8 -*-

from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from jkxymaven.items import JkxymavenItem
import os
from jkxymaven.XPATH import final_obtain_url

class Jkxymaven(CrawlSpider):  # 继承自CrawlSpider
    name = "jkxymaven"  # 给爬虫命名
    redis_key = 'jkxymaven:start_urls'
    start_urls = final_obtain_url()
    for eachurl in start_urls:
        def parse(self, response):
            seq = '5'
            ''' 在response已经爬取到了需要爬取的内容了，但是这里的body表示这个网页的源代码
            '''
            # print (response.body)
            # print (response.url)
            # print (type(response))
            # print (type(response.url))

            # response.url的值为'http://www.jikexueyuan.com/course/964.html'

            item = JkxymavenItem()  # 将类JkxymavenItem实例化成一个对象item

            ''' 使用Selector来处理response，就是网页返回的内容
                response其实是一个对象，它里面包括了很多属性
                把Selector(response)这个整体作为参数传递给selector
            '''
            selector = Selector(response)

            ''' 使用Movies变量保存从XPATH抓取到的所谓的先抓的“大”
            '''
            Movies = selector.xpath('//div[@id="wrapper"]/div[@id="pager"]/div[@class="lesson-table cf"]')

            for eachMoive in Movies:
                ''' 如果要把信息提取出来的话，那么需要在后面再加上.extract()这个方法，才能把信息提取出来
                '''
                title = eachMoive.xpath('div[@class="lesson-teacher"]/div[@class="bc-box"]/h2/a/text()').extract()[0] \
                    .replace(' ', '')
                movieInfo = eachMoive.xpath('div[@class="video-list"]/div[@class="lesson-box"]/ul/li/div/h2/a/text()') \
                    .extract()  # type (movieInfo) = list

                ''' quote可能为空，因此需要先进行判断
                    如果是空列表，直接使用[0]就会报错
                quote = eachMoive.xpath('div[@class="bd"]/p[@class="quote"]/span/text()').extract()
                if quote:
                    quote = quote[0]
                else:
                    quote = ''
                '''

                # createfolder = False  # switch if needed!!!
                # if createfolder:
                #     ''' 创建用来存储课件的文件夹
                #         e.g. "Python课程2.2-Python初级课程-Python语法基础"
                #     '''
                #     folder1 = u'd://pyRegularExpression//Results//Nagios课程'.encode('gbk') + seq + \
                #               u'-'.encode('gbk') + title.encode('gbk')
                #     folder = folder1 \
                #         .replace(' ', '') \
                #         .replace(u'（'.encode('gbk'), u'('.encode('gbk')) \
                #         .replace(u'）'.encode('gbk'), u')'.encode('gbk')) \
                #         .replace(u'——'.encode('gbk'), u'_'.encode('gbk')) \
                #         .replace(u'－'.encode('gbk'), u'_'.encode('gbk'))
                #     os.mkdir(folder)

                titleString = unicode(title).encode('utf-8')\
                    .replace('（', '(') \
                    .replace('）', ')')\
                    .replace('——', '_')\
                    .replace('－', '_')\
                    .replace('：', '_')\
                    .replace('、', '_')

                # movieInfoString = unicode(';'.join(movieInfo)
                #                           .replace(' ', '')).encode('utf-8') \
                #     .replace(u'（'.encode('utf-8'), '(') \
                #     .replace(u'）'.encode('utf-8'), ')')

                ''' Naming video lesson files
                '''
                i = 0
                a = movieInfo
                for eachvideofile in movieInfo:
                    a[i] = str(i + 1) + '.' + eachvideofile
                    i += 1
                videolessonfilename = unicode(';'.join(a)
                                          .replace(' ', '')).encode('utf-8') \
                    .replace(u'（'.encode('utf-8'), u'('.encode('utf-8')) \
                    .replace(u'）'.encode('utf-8'), u')'.encode('utf-8'))\
                    .replace(u'——'.encode('utf-8'), u'_'.encode('utf-8'))\
                    .replace(u'－'.encode('utf-8'), u'_'.encode('utf-8'))\
                    .replace(u'：'.encode('utf-8'), u'_'.encode('utf-8'))\
                    .replace(u'、'.encode('utf-8'), u','.encode('utf-8'))

                ''' 和字典的赋值很像
                '''
                item['title'] = titleString
                #item['movieInfo'] = movieInfoString
                item['videolessonfilename'] = videolessonfilename

                ''' 将item提交过去，并生成CSV文件
                '''
                yield item  # 生成到csv文件

        '''
        nextLink = selector.xpath('//span[@class="next"]/link/@href').extract()
        #第10页是最后一页，没有下一页的链接
        if nextLink:
            nextLink = nextLink[0]
            print (nextLink)
        '''

        ''' 回调函数，就是函数自身，有点像递归操作，通过这样的链接构造方式，
            把下一页的链接构造出来以后，重新传递给这个函数自己，再重新进行爬取
        '''
        # yield Request(self.url + nextLink, callback=self.parse)