#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-12-03 00:42:31
# @Author  : jiong (447991103@qq.com)
# @Version : $Id$


"""
实现功能：
1、爬虫
2、分词

输入：命令行模式 通过url 获取新闻正文
"""
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import requests
from lxml import etree


def get_url_news(url):
    # url = sys.argv[1]
    """
    最基础的
    获取搜狐新闻正文
    """
    r = requests.get(url)
    r.encoding = 'gbk'

    html = r.text.decode('utf-8')

    select = etree.HTML(html)
    # print html
    news = ''
    for each in select.xpath('//*[@id="contentText"]/div[1]/p'):
        news += each.xpath('string(.)').strip()

    return news


def get_news(path):
    """
    对输入url进行判断
    url or 文件名
    """
    if path.startswith('http'):
        print 'crawl news:---------------------------------'
        news = get_url_news(path)
        print news
        return news
    else:
        with open(path) as f:
            news = []
            i=1
            for each in f.readlines():
                each = each.strip()
                print 'crawl %d news:---------------------------------' %i
                print each
                news.append(get_url_news(each))
                i+=1

            return news


def test():
    test_url1 = 'http://stock.sohu.com/20161202/n474784977.shtml'
    test_url2 = 'url.txt'
    print get_url_news(test_url1)
    print get_news(test_url2)

if __name__ == '__main__':
    # url = sys.argv[1]

    print 'testing...'
    path = ''
    while 1:
        path = raw_input('please input url or file path (quit for exit):')

        if path == 'quit':

            print 'classify end'
            exit()
        else:
            news = get_news(each)
            print news
