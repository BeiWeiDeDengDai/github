# 选项卡管理


from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://zhangyinghao.real.hhzdev.com:8085/index")
browser.execute_script('window.open()')
browser.switch_to_window(browser.window_handles[1])

browser.close()
