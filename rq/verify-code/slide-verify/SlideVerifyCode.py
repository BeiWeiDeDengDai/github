import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
EMAIL = 'test@test.com'
PASSWORD = '123456'
imagesPath = "/Users/zhangyinghao/python-project/images/sc_%s.png"


class CrackGeetest():
    def __init__(self):
        print("开始进行初始化~~~~~")
        self.url = 'https://account.geetest.com/login'
        self.browser = webdriver.Chrome()
        self.browser.get(self.url)
        self.wait = WebDriverWait(self.browser, 15)
        self.email = EMAIL
        self.password = PASSWORD
    def get_geetest_button(self):
        print("获取按钮~~~")
        button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.geetest_btn_click')))
        return button

    def get_position(self, i):
        print("获取验证码位置")
        # 获取验证码位置，返回验证码位置元祖
        img = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.geetest_bg')))
        print(img)
        time.sleep(2)
        location = img.location
        size = img.size
        top, bottom, left, right = location['y'],location['y'] + size['height'], location['x'], location['x'] + size['width']
        print((top, bottom, left, right))
        sc = img.screenshot(imagesPath % i)
        # 截取
        try:
            sc.crop((top, bottom, left, right))
        except Exception as e:
            print("截图错误,忽略")
        return sc

    def verift(self):

            bool = True
            cnt = 0
            while (bool):
                try:
                    cnt += 1
                    # 获取按钮点击
                    button = self.get_geetest_button()
                    button.click()
                    self.get_position(cnt)
                    if (cnt == 10):
                        bool = False
                    print("获取位置成功， 开始开开去验证码图片")

                except Exception as e:

                    print("爬取错误%s, 正在第%s重试" % (e,cnt))
                    self.browser.refresh()



if __name__ == '__main__':
    cratchGeetest = CrackGeetest()
    cratchGeetest.verift()


