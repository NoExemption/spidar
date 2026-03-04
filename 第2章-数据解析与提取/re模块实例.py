import re

s = """
from re import findall<div class='方源'><span id='1'>古月</span></div>
<div class='天尊'><span id='2'>元始</span></div>
<div class='凝冰'><span id='3'>白</span></div>
<div class='青阳'><span id='4'>傅</span></div>
<div class='天王'><span id='5'>魔眼</span></div>
"""

obj = re.compile("<div class='.*?'><span id='.*?'>.*?</span></div>", re.S)  # re.S：让.能匹配换行符

lst = obj.finditer(s)
for i in lst:
    print(i.group())

# (?P<分组名字>正则)可以单独从正则匹配的内容中进一步提取内容
obj = re.compile("<div class='.*?'><span id='(?P<id>.*?)'>(?P<xing>.*?)</span></div>", re.S)  # re.S：让.能匹配换行符

lst = obj.finditer(s)
for i in lst:
    print(i.group("xing"))
    print(i.group("id"))