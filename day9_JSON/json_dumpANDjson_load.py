#coding=utf-8
import json
number=[2,7,8,3,4]
filename='number.json'
with open(filename,'w') as f:
    json.dump(number,f)            # json.dump()方法是将列表/字典转换为字符串类型，存储在json文件当中
with open(filename) as file:
    file1=json.load(file)          # json.load()方法是将字符串转换为原来的类型，把json文件加载到内存当中
print(type(number))    # 是列表类型
print(filename)
print(type(filename))  # 是字符串类型
print(file1)
print(type(file1))     # 是列表类型