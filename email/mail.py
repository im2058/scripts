#!/usr/bin/python 
# -*- coding:utf-8 -*-

#coding=utf-8
import smtplib
from email.mime.text import MIMEText
import time

tm= time.strftime('%m-%d',time.localtime(time.time()))
#msg_from='10438075@qq.com'                     #发送方邮箱
msg_from='shadow_vvip@qq.com'                     #发送方邮箱
passwd='equmrnizoiqhbgcg'                       #填入发送方邮箱的授权码
msg_to='10438075@qq.com'                      #收件人邮箱
#msg_to='m2058@sina.cn'                      #收件人邮箱
                            
subject="测试"
content="测试"   
msg = MIMEText(content)
msg['Subject'] = subject
msg['From'] = msg_from
msg['To'] = msg_to
try:
    s = smtplib.SMTP_SSL("smtp.qq.com",465)     #邮件服务器及端口号
    s.login(msg_from, passwd)
    s.sendmail(msg_from, msg_to, msg.as_string())
    print "successful"
except s.SMTPException,e:
    print "failed"
finally:
    s.quit()
