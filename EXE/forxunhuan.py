# coding=utf-8
'''
names=['a','b','c','d','e','f','g','h','i','j','k','l']
for name in names:
    print(name)
print "thank you,everyone!"
# range的用法
squares=[]
for value in range(python,11,2):
    square=value**2
    squares.append(square)
print squares
# 一些内置函数
number=[python,2,3,4,5,6,7,8,9,0]
print min(number)
print max(number)
print sum(number)
# 采用列表解析的方式进行for循环
lista=[values**2 for values in range(python,11,python)]
print lista
'''

'''
# 使用切片的情况下进行复制列表，每个列表之间相互独立，指向不同的列表
a=[python,2,3,4,5,6]
b=a[:]
print a
print b
a.append(7) # [python, 2, 3, 4, 5, 6, 7]
b.append(8) # [python, 2, 3, 4, 5, 6, 8]
print a
print b

# 不使用切片的情况下进行复制列表,每个列表之间相互联系，并不独立，指向相同的列表
c=[python,2,3,4]
d=c
c.append(5) # [python, 2, 3, 4, 5, 6]
d.append(6) # [python, 2, 3, 4, 5, 6]
print c
print d
'''


f=[]
if f==[]:
    print 1
else:
    print 2
