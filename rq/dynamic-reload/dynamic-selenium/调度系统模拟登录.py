import json
import time

import requests

from selenium import webdriver

browser = webdriver.Chrome()

# 首次打开token为空
browser.get(url='http://zhangyinghao.real.hhzdev.com:8085/index')

# 获取token
params = {
    'client_id': 'app-client',
    'client_secret': '123',
    'username': 'zhangyinghao',
    'password': 'zyhbwddd210',
    'grant_type': 'password'
}
get_token_url = 'http://duzhiyuan.real.hhzdev.com:8888/oauth/token'
resp = requests.post(url=get_token_url, params=params)
resp_result = json.loads(resp.content)
print(resp_result['access_token'])

# 将token 塞入 cookie中
cookie = {
    'name': 'Admin-Token',
    'value': resp_result['access_token']
}
browser.add_cookie(cookie)
time.sleep(5)
print("重新刷新页面")
browser.refresh()
time.sleep(5)

browser.delete_all_cookies() # 删除所有的cookies




