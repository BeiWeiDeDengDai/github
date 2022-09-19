# 延迟等待

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()

# 隐士等待
browser.implicitly_wait(10)
browser.get("https://ratel.haohaozhu.me/index.html")
print(browser.page_source)


# 显式等待
wait = WebDriverWait(browser, timeout=10) # 引入WebDriverWait对象， 指定最长等待时间，

#  然后调用它的until()方法， 传入要等待条件 (expected_conditions).  这里传入了 presence_of_element_located 代表节点出现的意思
#  其参数是 节点的定位元祖， 也就是 id 为 username的节点框
input = wait.until(EC.presence_of_element_located((By.ID, 'username')))
button = wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'button')))

print(input, button)
browser.close()


