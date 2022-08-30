import requests


url="https://www.baidu.com"
proxies={
    'http':'http://10.10.1.10:3128',
    'https':'http://10.10.1.10:1080'
}

res=requests.get(url, proxies)
res.encoding='utf-8'
print(res.text)

# proxies = {'https': 'http://user:password@10.10.1.10:3128/',}


