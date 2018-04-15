# coding=utf-8
# 声明一个列表
# sort方法是对列表当中的元素以字母的顺序进行排序的
names=['angular','bench','dic','cyww','xywq','tope','wqop','gille']
'''
names.sort(reverse=False)
print names
names.sort(reverse=True)
print names
'''

# sorted方法是对列表元素里面的顺序进行一个排序，而不是按照字母顺序进行排序的，对原来列表没有影响
a=sorted(names) # 默认是按照字母表正向排序
print(a)
print names
b=sorted(names,reverse=True) # reverse方法为TRUE时就进行反向排序
print(b)
print names
#  reverse方法直接用于列表后面，将会改变列表
names.reverse()
print(names)
names.reverse()
print(names)
print(len(names))
