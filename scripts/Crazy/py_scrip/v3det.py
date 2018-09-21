#!/usr/bin/python 
# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
import time
import os
import sys

tag = sys.argv[1]
url = sys.argv[2]
#url = 'https://www.youtube.com/channel/UC4rlAVgAK0SGk-yTfe48Qpw/videos'
print tag
print url
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
update_flag = 0
f=open('data/id_data','a+')
tm= time.strftime('%m/%d-%H:%M',time.localtime(time.time()))
try:
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
#    content =  response.read().decode('utf-8')
    content =  response.read()
    pattern = re.compile('video-time".*?watch\?v=(.*?)".*?hours',re.S)
    items = re.findall(pattern,content)
    f_con = f.read()
    print items
    for i in items:
        if (f_con.find(i) != -1 ):
            pass
        else:
            f.write(str(tag)+":  "+str(tm)+"\t"+"."+str(i)+"\n")
            update_flag = 1
    if (update_flag == 0):
        print "no update"
        f.write(str(tag)+":  "+str(tm)+"\t"+"there is no update! \n")
    f.close()
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason
