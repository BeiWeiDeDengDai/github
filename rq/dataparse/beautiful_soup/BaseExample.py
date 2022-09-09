from bs4 import BeautifulSoup


html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

# 简单语法
soup=BeautifulSoup(html, 'lxml')

# 将文本进行缩进输出 其实
print(soup.prettify())
# 获取标签喜爱p 以及其 文本 这样只会打印第一个
print(soup.p)
# 获取其属性h值
print("属性值: %s, name: %s" % (soup.p['class'], soup.p['name']))
print(soup.p.string)