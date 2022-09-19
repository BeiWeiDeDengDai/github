# 使用seleniumm操作cookies
import time

from selenium import webdriver


browser = webdriver.Chrome()

browser.get(url='https://realtime.haohaozhu.me/login?redirect=%2Frealtime%2Fmonitor')

print("添加前cookies:", browser.get_cookies())
cooikes = {
    'name':'username',
    'value':'zhangyinghao'
}
browser.add_cookie(cooikes)
print("添加cookies后: %s" % browser.get_cookies())

