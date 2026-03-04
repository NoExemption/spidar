import re

lst = re.findall("\\d+", "我的电话是1388254，我的朋友的电话是1522224")
print(lst)

# finditer:匹配字符串中所有的内容[返回的是迭代器],从迭代器中拿到内容需要.group()
it = re.finditer("\\d+", "我的电话是1388254，我的朋友的电话是1522224")
print(it)
for i in it:
    print(i)
    print(i.group())

# search返回的结果是match对象，拿到内容需要.group()，如果有多个匹配，则仅返回首个匹配项
s = re.search("\\d+", "我的电话是1388254，我的朋友的电话是1522224")
print(s.group())

# match是从头开始匹配
m = re.match("\\d+", "1388254，我的朋友的电话是1522224")
print(m.group())  # 不使用.group()则返回None，不会报错(第一个字符不是数字就会报错)

# 预加载正则表达式
obj = re.compile("\\d+")
ret = obj.finditer("我的电话是1388254，我的朋友的电话是1522224")
for i in ret:
    print(i.group())

Re = obj.findall("我的电话是1388254，我的朋友的电话是1522224")
print(Re)