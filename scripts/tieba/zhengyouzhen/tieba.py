#!/usr/bin/python 
# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
import time
import os
import sys
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf-8')

url = 'http://tieba.baidu.com/p/5547747968?share=9105&fr=share&see_lz=0&sfc=copy&client_type=2&client_version=9.3.8.0&st=1518269781&unique=D5379923'
pic_dir = 'pic1'

f=open('img_info','a')
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
headers = { 'User-Agent' : user_agent}
#update_flag = 0
tm= time.strftime('%m-%d\%H:%M',time.localtime(time.time()))
os.makedirs(str(pic_dir))
f.write(str(pic_dir)+' '+str(tm)+' '+str(url)+'\n')
try:
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    content =  response.read()
#    soup = BeautifulSoup(content).prettify()
#    f.write(str(soup))
#    print soup
    pattern = re.compile('post_content_main(.*?)user-hide-post-down',re.S)
    items = re.findall(pattern,content)
#    print items
    pattern1 = re.compile('src="(.*?)jpg',re.S)
    a='c'
    for i in a:
        imgs = re.findall(pattern1,items[0])
#        print imgs
        cnt = 1
        for img in imgs:
            img_url = str(img)+'jpg'
            urllib.urlretrieve(str(img_url),str(pic_dir)+"/"+str(cnt)+".jpg")
            cnt = cnt + 1
    f.close()
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason
