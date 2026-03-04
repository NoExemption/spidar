from lxml import etree

tree = etree.parse("Xpath解析入门.html")
# result = tree.xpath("/html")
# result = tree.xpath("/html/body/ul/li/a/text()")
# result = tree.xpath("/html/body/ul/li[1]/a/text()")  #Xpath的顺序是从1开始数的，而不是平常的0；[]表示索引
# result = tree.xpath("/html/body/ol/li/a[@href='yuanshitianzun']/text()")
# print(result)

# ol_li_list = tree.xpath("/html/body/ol/li")
#
# for li in ol_li_list:
#     # 从每个li中提取到文字信息
#     result1 = li.xpath("./a/text()")  # "./"表示在li中继续寻找，相对查找
#     result2 = li.xpath("./a/@href")
#     print(result1,result2)

print(tree.xpath("/html/body/ul/li/a/@href"))
