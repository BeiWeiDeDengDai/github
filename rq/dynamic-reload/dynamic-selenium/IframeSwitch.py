from selenium import webdriver



browser = webdriver.Chrome()

browser.get(url="https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")

try:
    print("切换子iframe")
    browser.switch_to_frame('iframeResult') # 切换 frame
    logo = browser.find_element_by_class_name("logo") # 根据class查找
    print(logo)
except:
    print("获取不到, 切换至父frame")
    browser.switch_to.parent_frame()
logo = browser.find_element_by_class_name("logo")
print('logo', logo.text)

browser.close()