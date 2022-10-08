import time

from selenium import webdriver



browser = webdriver.Chrome()

browser.get("https://ratel.haohaozhu.me/index.html")
input_name = browser.find_element_by_id('username') # 获取输入 用户名
input_ps = browser.find_element_by_id('password') # 获取输入 密码
submit = browser.find_element_by_xpath('//button[@type="submit"]') # 获取 登录

# print(browser.page_source)
# 节点交互
input_name.send_keys('孙旭')


input_name.clear() # 清空
input_name.send_keys('zhangyinghao') # 输入用户名

input_ps.send_keys('zyhbwddd210')  # 输入密码
submit.click() # 按钮点击
time.sleep(10)

# 关闭
browser.close()
