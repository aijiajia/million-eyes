#!/usr/bin/env python
# encoding: utf-8


"""
@version: 
@author: Herbert
@license: Apache Licence 
@contact: 
@site: 
@software: PyCharm
@file: seleniumMockLogin.py
@time: 2018/8/9 19:19
"""
import urllib
import time
import selenium
import sys

sel = selenium.webdriver.Chrome()
loginurl = 'http://weibo.com/'
# open the login in page
sel.get(loginurl)
time.sleep(10)

# sign in the username
try:
    sel.find_element_by_xpath("//div[@id='pl_login_form']/div/div[2]/div[1]/div[1]/input").send_keys('yourusername')
    print('user success!')
except:
    print('user error!')
time.sleep(1)
# sign in the pasword
try:
    sel.find_element_by_xpath("//div[@id='pl_login_form']/div/div[2]/div[2]/div[1]/input").send_keys('yourPW')
    print('pw success!')
except:
    print('pw error!')
time.sleep(1)
# click to login
try:
    sel.find_element_by_xpath("//div[@id='pl_login_form']/div/div[2]/div[6]/a").click()
    print('click success!')
except:
    print('click error!')
time.sleep(3)
curpage_url = sel.current_url
print(curpage_url)
while (curpage_url == loginurl):
    # print 'please input the verify code:'
    print('please input the verify code:')
    verifycode = sys.stdin.readline()
    sel.find_element_by_xpath("//div[@id='pl_login_form']/div/div[2]/div[3]/div[1]/input").send_keys(verifycode)
    try:
        sel.find_element_by_xpath("//div[@id='pl_login_form']/div/div[2]/div[6]/a").click()
        print('click success!')
    except:
        print('click error!')
    time.sleep(3)
    curpage_url = sel.current_url
# get the session cookie
cookie = [item["name"] + "=" + item["value"] for item in sel.get_cookies()]
# print cookie

cookiestr = ';'.join(item for item in cookie)
print(cookiestr)

print('%%%using the urllib2 !!')
homeurl = sel.current_url
print('homeurl: %s' % homeurl)
headers = {'cookie': cookiestr}
req = urllib.Request(homeurl, headers=headers)
try:
    response = urllib.urlopen(req)
    text = response.read()
    fd = open('homepage', 'w')
    fd.write(text)
    fd.close()
    print('###get home page html success!!')
except:
    print('### get home page html error!!')
