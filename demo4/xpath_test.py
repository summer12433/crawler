# -*- coding: utf-8 -*-
# @Time    : 2020/8/13 21:47
# @Author  : summer
# @File    : xpath_test.py

from lxml import etree

html_doc = """
<?xml version="1.0" encoding="ISO-8859-1"?>

<bookstore>

<book category="COOKING">
  <title lang="en">Everyday Italian</title>
  <author>Giada De Laurentiis</author>
  <year>2005</year>
  <price>30.00</price>
</book>

<book category="CHILDREN">
  <title lang="en">Harry Potter</title>
  <author>J K. Rowling</author>
  <year>2005</year>
  <price>29.99</price>
</book>

<book category="WEB">
  <title lang="en">XQuery Kick Start</title>
  <author>James McGovern</author>
  <author>Per Bothner</author>
  <author>Kurt Cagle</author>
  <author>James Linn</author>
  <author>Vaidyanathan Nagarajan</author>
  <year>2003</year>
  <price>49.99</price>
</book>

<book category="WEB">
  <title lang="en">Learning XML</title>
  <author>Erik T. Ray</author>
  <year>2003</year>
  <price>39.95</price>
</book>

</bookstore>"""

#创建HTML对象
html = etree.HTML(html_doc)

#获取html节点
print(html.xpath("/html"))
#获取根节点
print(html.xpath("/"))
#获取当前节点位置
print(html.xpath("."))
#获取第一个book节点
print(html.xpath("/html/body/bookstore/book[1]"))
#获取倒数第一个book节点
print(html.xpath("/html/body/bookstore/book[last()]"))
#文档任意位置匹配book节点
print(html.xpath("//bookstore/book[1]"))

#获取标签的属性值(cooking)
print(html.xpath("//bookstore/book[1]/@category"))

#获取所有的book节点的属性值
print(html.xpath("//bookstore/book/@*"))

