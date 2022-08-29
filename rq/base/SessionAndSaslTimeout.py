import requests
import urllib3

url = "https://www.baidu.com"

# 忽略警告
urllib3.disable_warnings()

# timeout 表示 连接 和 读取
# 如果只是指定一个值  timeout = 2    则代表连接和读取总
# timeout = None 代表永久
requests.get(url, timeout=(2, 10), verify=False)