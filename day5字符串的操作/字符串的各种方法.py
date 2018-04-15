# coding=utf-8

 # find()函数用于查找在某一个字符串当中的某一个字符，默认从字符串从左至右找
myname="hello world python!"
print(myname.find("python"))  # 如果能够找到，得到的是要匹配的字符串的第一个字符所处的下标位置
print(myname.find("python1")) # 如果找不到，就会返回-1
 # rfind()函数用于查找在某一个字符串当中重复的字符，从右边开始查找
mystr="hello world python,I love python!"
print(mystr.rfind("python"))
# index()方法也是查找字符的，也是默认从左至右开始找
mystr2="hello world test,I love test!"
print(mystr2.index("test"))
# 同样的，index()方法也有rindex()方法来进行从右至左进行查找
print(mystr2.rindex("test"))

# count()方法用于统计某一个字符在字符串当中出现的次数
print(mystr.count("python"))
print(mystr2.count("test"))
# replace()方法用于替换字符串当中的某一个字符串，可以指定替换次数,这里的替换是临时性的
print(mystr.replace("hello","good"))
print(mystr2.replace("test","good",1)) # 即使字符串当中有多个被替换的字符，但是这里可以指定替换的次数
# split()方法用于分割字符串，括号里面跟以什么进行分割的符号
print(mystr.split(" "))  # 这里是以空格分割
print(mystr2.split(" ",2))  # 这里的数字是指下标，意思是将整个字符串分割为3段字符串

