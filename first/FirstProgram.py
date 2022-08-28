from urllib.request import urlopen

url = "http://www.baidu.com"
response = urlopen(url) # 打开百度

# 创建文件
with open("mybaidu.html", mode="w") as f:
    f.write(response.read().decode("utf-8")) #保存在文件中
print("done")