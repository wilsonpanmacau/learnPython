# coding=utf-8
i=int(input(u"请输入行数"))
a=0
while a<i:
    b=0
    while b<a:
         print "",
         b+=1
    c=i-a;
    while c>0:
         print "*",
         c-=1
    print " "
    a+=1
