# 百度翻译
import requests

url = "https://fanyi.baidu.com/sug"

card = input("请输入你要翻译的单词")
card_dic = {
    "kw": card
}
# post 方法
resp = requests.post(url, data=card_dic)
print(resp.json()) # 将服务器返回的内容直接处理成json => dict
resp.close()