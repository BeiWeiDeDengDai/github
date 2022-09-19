import time

from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
time.sleep(3)
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
browser.execute_script('alert("到最底部了")')

time.sleep(10)
browser.close()