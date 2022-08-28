import requests

import re

url = "https://28daoaa.com/"
headers ={
    "User-Agent": "Mozilla"}
resp = requests.get(url, headers=headers)
resp.encoding = "utf-8"

print(resp.text)

re_compile = re.compile(r'.*?<div class="card mb-0">.*?<a href="(?P<link>.*?)" class="videoinfo">'
                        r'.*?<p class="text-muted mb-0 pb-0">(?P<title>.*?)</p>'
                        r'', re.S)
results = re_compile.finditer(resp.text)

for it in results:
    if (it.group("title")==""):
       print("错误")
    else:
        print("link: %s%s ,title: %s" % (url,it.group("link"), it.group("title")))