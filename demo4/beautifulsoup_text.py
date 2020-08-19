# -*- coding: utf-8 -*-
# @Time    : 2020/8/12 23:01
# @Author  : summer
# @File    : beautifulsoup_text.py


from bs4 import BeautifulSoup as bs


html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

#1. 创建Soup对象,第一个是解析对象，第二个参数是解析器
soup = bs(html_doc, "lxml")

#打印规范的格式
print(soup.prettify())
#打印title
print(soup.title)
#打印title名字
print(soup.title.name)
#打印title的文本信息
print(soup.title.string)
#打印title父标签文本信息
print(soup.title.parent.string)
#匹配第一个p标签
print(soup.p)
#匹配所有的p标签
print(soup.find_all("p"))
#返回匹配的第一个p标签
print(soup.find("p"))
#获取标签的文本信息
print(soup.p.get_text())


#提取属性
print(soup.a["href"])
#提取具体属性
print(soup.find(id="link2"))

#查看类型
print(type(soup.a))

#提取注释信息
print(type(soup.title.string))

#contents返回当前标签下面的直接子节点,返回列表,常用
print(soup.find("p", attrs={"class": "story"}).contents)
#children返回当前标签下面的对象的迭代器，使用list转换
print(list(soup.find("p", attrs={"class": "story"}).children))
#descendants获取标签下面的所有子节点的生成器，list转换
print(list(soup.find("p", attrs={"class": "story"}).descendants))

#返回p标签下面的所有文本信息，包括换行
print(list(soup.p.strings))

#返回多个父节点
print(list(soup.title.parents))

#返回下一个兄弟标签
print(repr(soup.p.next_sibling))
#返回下一个所有的兄弟标签,返回迭代器
print(list(soup.p.next_siblings))
#返回上一个兄弟标签
print(repr(soup.p.previous_sibling))

#返回所有的要查找的标签
print(soup.find_all(["p", "a"]))
#返回所有的要查找的文本
print(soup.find_all(text="Lacie"))
#返回要查找符合条件的标签,class是关键字
print(soup.find_all("p", attrs={"class": "story"}))
print(soup.find_all("p", id="link2"))


