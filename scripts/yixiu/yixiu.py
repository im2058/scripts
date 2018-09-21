#!/usr/bin/python 
# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
import time
import os
import sys

urlb = 'http://www.tu11.com'
url = 'http://www.tu11.com/meituisiwatupian/'
print url
f=open('img_url','w')
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
headers = { 'User-Agent' : user_agent}
#update_flag = 0
tm= time.strftime('%m-%d',time.localtime(time.time()))
tm='02-03'
try:
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    content =  response.read()
    pattern = re.compile('target="_blank"><b>.*?href="(.*?)".*?'+str(tm),re.S)
    items = re.findall(pattern,content)
#    print items
    a='c'
    for i in items:
        url1 = str(urlb)+str(i)
#        print url1
#        url1 = 'http://www.tu11.com/BEAUTYLEGtuimo/2018/10567.html'
        request1 = urllib2.Request(url1,headers = headers)
        response1 = urllib2.urlopen(request1)
        content1 =  response1.read()
#        soup = BeautifulSoup(content1).prettify()
#        print soup
        pattern1 = re.compile('center.*?img\ src="(.*?)"\ /></p',re.S)
#        pattern1 = re.compile(str(tm)+'.*?img\ src="(.*?)"\ /></p',re.S)
        img_url = re.findall(pattern1,content1)
        print img_url[0]
        f.write(str(img_url[0])+'\n')
    f.close()
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason
