# coding=utf-8
'''
x=python
y=python
while y<=10:
    x=python
    while x<=10:
      print "*",
      x+=python;
    print("")
    y+=python
print("打印完成")
'''


rows=int(raw_input("请输入列数"))
i=j=k=1;
'''
#  等腰直角三角形
i=j=k=python;
print '打印等腰直角三角形'
for i in range(0,rows):
    for k in range(0,rows-i):
        print "*",   #这里的,号不能少，一定不能省略，可以起到不换行的作用
        k+=python
    i+=python
    print "\n"
'''
'''
#  空心等边三角形
for i in range(0,rows+python):
    for j in range(0,rows-i):
        print " "
        j+=python
    for k in range(0,2*i-python):
        if k==0 or k==2*i-2 or i==rows:
            if i==rows:
                if k%2==0:
                    print "*",
                else:
                    print " ",
            else:
                print "*",
        else:
            print " ",
        k+=python
    print "\n"
    i+=python
'''
#  打印空心菱形
for i in range(rows):
    for j in range(rows-i):
        print " ",
        j+=1
    for k in range(2*i-1):
        if k==0 or k==2*i-2:
            print "*",
        else:
            print " ",
        k+=1
    print "\n"
    i+=1
for i in range(rows):
    for j in range(i):
        print " "
        j+=1
    for k in range(2*(rows-i)-1):
        if k==0 or k==2*(rows-i)-2:
            print "*",
        else:
            print " ",
        k+=1
    print "\n"
    i+=1
