#coding=utf-8
# 不指明已知文件打开方式
# with open('test.txt') as fileObj:
#     contents=fileObj.read()
#     print(contents)
# 指明已知文件打开方式
with open('test.txt','r') as f:
    print(f.read().strip())
# 直接创建新的文件
with open('test1.txt','w')as f1:
    pass
# # 打开文件也有以下这种方式,但是这种方式目前不采用
# f=open('test.txt','r')
# content=f.read()
# print("111")
# f.close()
