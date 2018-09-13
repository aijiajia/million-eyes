#!/usr/bin/env python
# encoding: utf-8


"""
@version: 
@author: Herbert
@license: Apache Licence 
@contact: 
@site: 
@software: PyCharm
@file: seleniumDemo.py
@time: 2018/8/9 16:17
"""


from selenium import webdriver

#浏览器驱动
# driver=webdriver.Firefox()
driver=webdriver.Chrome()

driver.get("https://www.baidu.com")

driver.find_element_by_id("kw").send_keys("Selenium2")
driver.find_element_by_id("su").click()
driver.quit()