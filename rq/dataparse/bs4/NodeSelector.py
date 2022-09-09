# 嵌套选择

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
"""

from bs4 import BeautifulSoup

resp = BeautifulSoup(html, "lxml")

print("打印头节点标签 %s" % resp.head)
print("打印头节点标签值 %s" % resp.head.string)
print("打印头节点嵌套标签 %s" % resp.head)



# 关联选择
html = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 
            and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
        <p class="story">...</p>
"""
resp = BeautifulSoup(html, "lxml")

# 打印全文中p节点
print("打印全文中p节点 列表形式返回" % resp.p.contents)
print("################################################ 子节点 ################################################ ")

# 遍历p节点  ################################# 子节点
for i, child in enumerate(resp.p):
    print("第%s个节点, 节点为: %s" % (i, child))
print("################################################ 子节点和子孙结点 ################################################ ")

#  遍历p 节点  ################################# 子节点   子孙节点 descendants
for i, child in enumerate(resp.p.descendants):
    print("第%s个节点, 节点为: %s" % (i, child))

# 父节点和祖先节点  ################################# 子节点
html = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
        </p>
        <p class="story">...</p>
"""
print("################################################ 父节点和祖先节点 ################################################ ")
soup = BeautifulSoup(html, 'lxml')

print("parent 父节点 ", soup.a.parent)
print("parents 祖先节点 ", soup.a.parents)

print("################################################ 兄弟节点 ################################################ ")

html = """
<html>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
            Hello
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 
            and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
"""
sou = BeautifulSoup(html, "lxml")
print("next 节点 sibling", sou.a.next_sibling)
print("prev 节点 sibling", sou.a.previous_sibling)

print("所有 next 节点 siblings", list(enumerate(sou.a.next_siblings)))
print("所有 prev 节点 siblings", list(enumerate(sou.a.previous_siblings)))

print("################################################ 关联节点相关属性 ################################################ ")

html = """
<html>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">Bob</a><a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 
        </p>
"""
soup = BeautifulSoup(html, "lxml")
print("a的父亲节点:", list(soup.a.parents)[0]['class'])
