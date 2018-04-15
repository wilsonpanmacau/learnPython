#coding=utf-8
#-------------------------------------复制文件--------------------------------------
# 源文件
source_file="test.txt"
# 目标文件给予命名
dest_file="copy-"+"test.txt"
# 打开源文件进行读取
with open(source_file) as source_f:
    content=source_f.read()
# 新建并打开目标文件，将源文件的数据写入目标文件
with open(dest_file,"w") as dest_f:
    dest_f.write(content)   #至此文件就copy好了