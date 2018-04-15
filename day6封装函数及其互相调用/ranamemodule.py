#coding=utf-8
#给模块起别名
import makepizza as mk
mk.make_drink(22,"ptatos","water","zhong")
a=100
print(id(a))
def change():
    a=200
    print(a)
    print(id(a))
change()
print(a)
print(id(a))