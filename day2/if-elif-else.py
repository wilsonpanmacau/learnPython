#coding=utf-8
age=input(u"请输入年龄：")
sex=raw_input(u"请输入性别：")
if age>=18 and sex==u"男":
    print(u"你是成年男子")
elif age<18 or sex==u"女":
    print(u"你是小女孩")
else:
    pass # 便于将来填充代码，这里先留下，不至于语法错误

