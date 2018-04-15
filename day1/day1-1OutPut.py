# coding=utf-8
# 变量
# 导入关键字，输出关键字列表
import keyword
print keyword.kwlist
a='aaa'
x,y,z=11,22,5
print x
print y
print z
print type(x);
print type(a);
# 如果要统一输出的规范，我们需要人为规定输出的都是多少位数的；
money=22;
print ('woyouqian:%04d元钱'%money)# 在这里的0代表用0来站位置，4代表输出的位数，不够4位的用0来填充；
# 精确到小数点后面多少位数，不够位数用一个数来填充怎么办？
w=3.1415926
print('圆周率是：%.4f'%w)# .代表小数点，4代表精确到小数点的第几位，f代表浮点数，这里是四舍五入的算法
a=35;
b=36;
c=37;
myName="caimingliang"
print("我的年龄为:%s岁"%(b+c));# b+c必须要加上括号，否则会先将b作为参数带入计算，再来将c作为另外一个数据；
print("我的年龄是:%s岁,我的姓名是：%s"%(a+b,myName));


