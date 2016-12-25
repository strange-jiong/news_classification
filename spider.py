# -*- coding:utf-8 -*-
'''
Created on 2016-12-18
@author: 
'''

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import urllib2
from bs4 import BeautifulSoup
import socket
import httplib


class Spider(object):
    """Spider"""

    def __init__(self, url):
        self.url = url

    def getNextUrls(self):
        urls = []
        request = urllib2.Request(self.url)
        request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; \
            WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36')
        try:
            html = urllib2.urlopen(request).read()
        except socket.timeout, e:
            pass
        except urllib2.URLError, ee:
            pass
        except httplib.BadStatusLine:
            pass

        soup = BeautifulSoup(html, 'html.parser')
        for link in soup.find_all('a'):
            print("http://m.sohu.com" + link.get('href'))
            if link.get('href')[0] == '/':
                urls.append("http://m.sohu.com" + link.get('href'))
        return urls


def getNews(url):
    print url
    xinwen = ''
    request = urllib2.Request(url)
    request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; \
        WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36')
    try:
        html = urllib2.urlopen(request).read()
    except urllib2.HTTPError, e:
        print e.code

    soup = BeautifulSoup(html, 'html.parser')
    for news in soup.select('p.para'):
        xinwen += news.get_text().decode('utf-8')
    return xinwen


class News(object):
    """
    source:from where 从哪里爬取的网站
    title:title of news  文章的标题    
    time:published time of news 文章发布时间
    content:content of news 文章内容
    type:type of news    文章类型
    """

    def __init__(self, source, title, time, content, type):
        self.source = source
        self.title = title
        self.time = time
        self.content = content
        self.type = type


def setProxy(pro):
    proxy_support = urllib2.ProxyHandler({'https': pro})
    opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler)
    urllib2.install_opener(opener)


def getHtml(url, pro):
    urls = []

    request = urllib2.Request(url)
    setProxy(pro)
    request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; \
        WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36')

    try:
        html = urllib2.urlopen(request)
        statusCod = html.getcode()
        if statusCod != 200:
            return urls
    except socket.timeout, e:
        pass
    except urllib2.URLError, ee:
        pass
    except httplib.BadStatusLine:
        pass

    return html

file = open('test1.txt', 'a')
for i in range(38, 41):
    for j in range(1, 5):
        url = "http://m.sohu.com/cr/" + str(i) + "/?page=" + str(j)
        print url
        s = Spider(url)
        for newsUrl in s.getNextUrls():
            file.write(getNews(newsUrl))
            file.write("\n")
            print "---------------------------"
