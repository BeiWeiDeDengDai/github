from lxml import etree

text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''

html = etree.HTML(text)
print(etree.tostring(html))

# 文本获取 /text()
# 获取孙节点 使用两个//  //ul//a
print("获取子节点 " + html.xpath("//li/a/text()")[0]) #获取子节点 first item
print("获取子孙节点 " + html.xpath("//ul//a/text()")[0]) # 获取子孙节点 first item
# 获取父节点
#['item-0', 'item-1', 'item-inactive', 'item-1', 'item-0']
print( html.xpath("//a/../@class"))
# 使用 parent::获取父节点
#['item-0', 'item-1', 'item-inactive', 'item-1', 'item-0']
print (html.xpath("//a/parent::*/@class"))

# 属性匹配 限制 文本中只有两个属性是 item-1
#[<Element li at 0x1106f2308>, <Element li at 0x1106f2348>]
print(html.xpath('//li[@class="item-1"]'))


# 文本内容获取  # 结果有一个\n 是因为 有一个li 是自动修订的 所以会有
# ['first item', 'second item', 'third item', 'fourth item', 'fifth item', '\n     ']
print(html.xpath("//li//text()"))
# 选取最细粒度的不存在这个问题 的
# ['first item', 'second item', 'third item', 'fourth item', 'fifth item']
print(html.xpath("//li/a/text()"))

# 属性匹配
#['link1.html', 'link2.html', 'link3.html', 'link4.html', 'link5.html']
print(html.xpath("//li/a/@href"))

# 属性多值匹配   class里面有两个 li li-first 如果用之前的方式无法匹配 需要使用containers
# ['first item']
text = '''  
<li class="li li-first"><a href="link.html">first item</a></li> 
'''
html=etree.HTML(text)
print(html.xpath('//li[contains(@class, "li")]/a/text()'))

# 多属性匹配
text = '''  
<li class="li li-first" name="item"><a href="link.html">first item</a></li>
'''
html=etree.HTML(text)
print(html.xpath('//li[contains(@class, "li") and @name="item"]/a/text()'))



