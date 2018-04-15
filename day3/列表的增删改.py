# coding=utf-8
# 声明一个列表
names=[1,2,3,4,5,'6']
print(names[0]);
# 列表元素的添加
  # 第一种方法是在末尾添加，使用append()方法；
names.append(6)
print(names);
  # 第二种方法是在指定位置添加，使用insert()方法，此方法有两个参数，一个是下标，一个是添加的元素的值；
lists=['A','B','C','D']
lists.insert(2,'E')
print(lists)
  # 第三种方法是进行列表的合并，使用extend()方法
list1=[1,2,3,4,5,6,7];
list2=['F','G','R','W','T','U'];
list1.extend(list2);
print(list1) # 将list2当中的元素合并到list1当中来了
print(list2)

# 列表元素的删除
  # 第一种方法是在末尾删除元素，使用pop()方法
people=['张三','李四','王五','赵六'];
people.pop()
print(people)
  #第二种方法是直接指出下标位置，也可以删除整个列表
del people[0]
print(people)
  # 第三种方法是直接指出元素的值，进行删除,但是这个方法只能删除列表当中第一个
  # 满足这个值的元素，如果列表当中有多个这样的元素，就需要进行循环遍历进行删除；
people.remove('李四')
print(people)


