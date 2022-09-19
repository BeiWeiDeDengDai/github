# 获取节点信息
import time

from selenium import webdriver
from selenium.webdriver import ActionChains


browser = webdriver.Chrome()
url = 'https://www.zhihu.com/explore'
browser.get(url)

id = browser.find_element_by_id('js-clientConfig')
print(id)
print(id.get_attribute('type')) # 获取属性值

search = browser.find_element_by_class_name('ExploreHomePage-specialsLoginBottomButton')
print(search.text) # 获取文本值

search = browser.find_element_by_id('Popover1-toggle')
print("search id", search.id)
print("search location", search.location)
print("search tag_name", search.tag_name)
print("search size", search.size)


time.sleep(10)
browser.close()
