# 京东信息获取
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pyquery import PyQuery as pq
params = {
    'keyword': 'iphone14'
}

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 20)

def get_product_info():
    html = browser.page_source
    doc = pq(html)
    items = doc('#J_goodsList .gl-warp li div').items()
    for item in items:
        mobile_info = {
            'price': item.find('.p-price').text(),
            'title': item.find('.promo-words').text(),
            'comment': item.find('.p-commit').find('a').text(),
            'shop': item.find('.curr-shop').attr('title')
        }
        if (item.find('.p-price').text() != ''):
            # print(item)
            print(mobile_info)


# 获取相应内容
def index_page(page):
    print('正在爬取', page, '页')
    try:
        url = 'https://search.jd.com/Search?keyword=' + params['keyword']
        browser.get(url)
        browser.maximize_window()
        if (page > 1):
            # 获取页面输入框
            # page_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.p-skip .input-txt')))
            # page_input = wait.until(EC.presence_of_element_located((By.XPATH, '//span[@class="p-skip"]/input')))
            # 搜索输入框
            # page_input = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="form"]/input')))
            # page_input = browser.find_element_by_xpath('//span[@class="p-skip"]/input')
            # print("page input", page_input)
            # # 获取确定按钮框
            #
            # page_input.clear()
            # page_input.send_keys(page)
            print("输入页码:", page)
            sure_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.p-num .pn-next')))
            print("sure_button", sure_button.text)
            sure_button.click()
            time.sleep(2)
        # 获取高亮  text_to_be_present_in_element 判断某个元素中的text是否包含了预期的字符串
        res = wait.until(EC.presence_of_element_located((By.XPATH, '//span[@class="p-num"]/a[@class="curr"]')))
        print("当前页码", res.text)
        if (res.text == str(page)) :
            # pattern_result = wait.until(EC.text_to_be_present_in_element((By.XPATH, '//span[@class="p-num"]/a[@class="curr"]'), str(page)))
            # print("匹配结果: ", pattern_result)
            print("匹配成功")
        else:
            print("失败")
        # 直到获取有列表信息
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#J_goodsList .gl-warp li')))
        print('爬取成功，开始解析')
        get_product_info()
        # browser.close()
    except Exception as e:
        print("爬取失败, %s" % e)
        browser.close()


if __name__ == '__main__':
    index_page(2)