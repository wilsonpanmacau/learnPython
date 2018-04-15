#coding=utf-8
# 从某个目录下去找包含有“hello”的.py文件有哪些？
import os
file_list=[]
def find_hello(parent_dir,file_name):
    file_abspath=os.path.join(parent_dir,file_name)
    if os.path.isdir(file_abspath):
        for f in os.listdir(file_abspath):
            find_hello(file_abspath,f)
    else:
        if file_abspath.endswith('.py'):
            if read_and_find_hello(file_abspath):
                file_list.append(file_abspath)


# 这个函数主要是读取以.py结尾的文件，看文件当中是否包含有hello，如果有就返回True,没有就返回False
def read_and_find_hello(py_file):
    flag=False
    f=open(py_file)
    while True:
        line=f.readline()
        if line=='':
            break
        elif "hello" in line:
            flag=True
            break
    f.close()
    return flag


