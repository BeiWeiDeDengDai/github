
import requests

url="https://movie.douban.com/j/chart/top_list"



# 重新封装参数
params = {
    "type": 5,
    "interval_id": "100:90",
    "action": "",
    "start": 0,
    "limit": 20,
}
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}
# params 是针对 get请求的    data 针对post, 如果有反爬的 那我们需要使用 ua
resp = requests.get(url=url, params=params, headers=headers)
print(resp.request.url) # 打印封装好的url
print(resp.request.headers) # 打印请求头
print(resp.json()) # 结果格式化
resp.close()