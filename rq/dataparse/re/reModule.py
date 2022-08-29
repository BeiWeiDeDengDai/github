import re


# findall: 匹配字符串中所有的符合正则的内容
str = "我的电话好 19110449632, 女朋友电话好 18853544805"
print(re.findall(r"\d+", str))


# finditer: 匹配字符串中所有的内容 【返回的是迭代器】
# 从迭代器拿取内容 group()
it = re.finditer(r"\d+", str)
for i in it:
    print("it 匹配: %s" % i.group())

# 找到一个内容就返回
seach = re.search(r"\d+", str)
print("search 匹配: %s" % seach.group())

# 从头开始匹配
try:
    match = re.match(r"\d+", str)
    print("match 匹配: %s" % match.group())
except:
    print("出错了")


# 预加载正则
obj = re.compile(r"\d+")
comp = obj.search(str)
print("comp 匹配: %s" % comp.group())


s="""
<div class='jay'><span id='1'>周杰伦</span></div>
<div class='zyh'><span id='2'>张英豪</span></div>
<div class='sx'><span id='3'>小九</span></div>
"""
# re。S 让.能够匹配换行符
# () 可以把正常归类组 并且可以给组起名字  (?P<分组名字>正则)
div_comp = re.compile(r"<div class='(?P<class>.*?)'><span id='(?P<id>\d+)'>(?P<name>.*?)</span></div>", re.S)


res = div_comp.finditer(s)

for i in res:
    # print(i.group())
    #print(i.group("class"))
    print("class: %s, id: %s, name: %s" % (i.group("class"), i.group("id") , i.group("name")))