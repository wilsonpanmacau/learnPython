# coding=utf-8
# a=raw_input('请输入数据');括号里面的是提示语，提示用户的,只在Python2当中有，它负责字符串
'''
a=raw_input("请输入内容：");
print(a+"111");
# input('请输入数据');在Python2、python3当中都有，在Python2当中输入的内容作为表达式
b=input("请输入内容：")
print(b)
'''
# 在python2当中使用raw_input(),都会当做字符串
name=raw_input("请输入姓名：") # 这里输入的是字符串
print(type(name))
age=input("请输入年龄：") # 这里输入的是数字
print(type(age))
print("我的姓名是：%s，我的年龄是：%d"%(name,age));


