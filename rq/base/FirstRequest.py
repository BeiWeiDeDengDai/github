import requests





query = input("输入喜欢的明星")
# 定义一个网址
url = f"https://www.sogou.com/web?query={query}"

# 定义请求头 避免以为是机器
headers_dic = {
"user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}

# 使用 requests 工具包 获取
resp = requests.get(url, headers= headers_dic)


print(resp.text) # 拿到网页源代码
resp.close()