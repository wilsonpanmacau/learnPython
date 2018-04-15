# coding=utf-8
# 使用sort()方法对列表进行排序，这种排序是永久性的
cars=['BMW','AUDI','TOYOTA','HONDA']
cars.sort()
print(cars)  # 这样排序出来的是按照字母的排序的，即使是以字符串的显示来排列的
number=[1,4,3,9,5,6,7,8]
# 使用sorted()方法对列表进行排序，这种排序是临时性的
print(sorted(number))
print(number)