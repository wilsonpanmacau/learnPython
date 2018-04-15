# coding=utf-8
x=1 # 代表行
while x<=9:  # 一共要循环9次才能打印9行，每行打印的列数和行号一致
    y=1 #代表列
    while y<=x:
        print "%d*%d=%d\t"%(y,x,x*y),
        y+=1
    print " "
    x+=1
print 'over'
