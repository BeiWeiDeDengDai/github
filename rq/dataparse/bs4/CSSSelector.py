from bs4 import BeautifulSoup

html='''
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
            <li class="sx">Foo</li>
            <li class="zyh">Bar</li>
        </ul>
    </div>
</div>
'''

soup = BeautifulSoup(html,"lxml")

# 选择 ul li 节点  返回的是一个列表
print("选择ul li 节点", soup.select("ul li"))

for ul in soup.select("ul"):
    for li in ul.select("li"):
        print("li值", li.string)
        print("li name属性", li['class'])