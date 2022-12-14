from selenium import webdriver
from selenium.webdriver import ActionChains


browser = webdriver.Chrome()

browser.get("http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")

browser.switch_to_frame('iframeResult')

source = browser.find_element_by_css_selector('#draggable')
target = browser.find_element_by_css_selector('#droppable')

actions = ActionChains(browser)

actions.drag_and_drop(source, target)
actions.perform()

