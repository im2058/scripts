#!/usr/bin/python
## -*- coding: utf-8 -*-
import sys
sys.path.append('/home/pi/.local/lib/python2.7/site-packages')
from pytube import YouTube
import urllib
from pprint import pprint
import os
import re

vid = sys.argv[1]
#vid = 'rCXPSrcnozk'
yt = YouTube("\"http://www.youtube.com/watch?v="+str(vid)+"\"") 
print(yt.title)
#print(yt.video_id)
#yt.set_filename('myFirstVideo')
#pprint(yt.filter('flv'))
#print(yt.filter('.mp4')[-1])
#pprint(yt.filter(resolution='480p'))
#video =yt.streams('mp4','720p')
video = yt.streams.first()
#video = yt.filter('.mp4')[-1]
video.download('/mnt/usb/download/Gucci')
