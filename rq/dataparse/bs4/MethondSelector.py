from bs4 import BeautifulSoup

html = '''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''

soup = BeautifulSoup(html, 'lxml')

# 方法选择器 find find_all
print("所有ul", soup.find_all(name="ul"))
# 每个元素是 bs4.element.Tag 类型
print(type(soup.find_all(name="ul")[0]))

for it in soup.find_all(name="ul"):
    print("ul下节点遍历", it.find_all(name="li"))

print("遍历ul -> li 下元素节点")

for ul in soup.find_all(name="ul"):
    for li in ul.find_all(name="li"):
        print("li节点:", li.string)
print("通过 属性来进行查询")

print("属性通过id 锁定", soup.find_all(attrs={'id': 'list-1'})) # 类型  <class 'bs4.element.ResultSet'>
print("属性通过class索引", soup.find_all(attrs={'class': 'element'})) # 类型  <class 'bs4.element.ResultSet'>

# text 选择
html='''
<div class="panel">
    <div class="panel-body">
        <a>Hello, this is a link</a>
        <a>Hello, this is a link, too</a>
    </div>
</div>
'''
soup = BeautifulSoup(html, "lxml")
import re

# 返回了两个包含link的
print(soup.find_all(text=re.compile('link')))


###################################### find 方法
# find 返回的都是单个元素，也就是第一个匹配到的元素 find_all 返回的是所有匹配元素组成的列表

