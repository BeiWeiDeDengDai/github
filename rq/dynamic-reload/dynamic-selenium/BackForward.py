# 前进后退方法的使用
import time

from selenium import webdriver

browser = webdriver.Chrome()

browser.get("https://ratel.haohaozhu.me/index.html")
browser.get("https://realtime.haohaozhu.me/login?redirect=%2Frealtime%2Fmonitor")
browser.get("https://www.baidu.com")


# 后退
browser.back()

time.sleep(2)

browser.forward()
time.sleep(2)
browser.close()