# coding=utf-8

arr=[1,89,34,72,5,119,23,53]
leng=range(len(arr))[::-1]
print leng
for i in leng:
    for j in range(i):
        if arr[j]>arr[j+1]:
            arr[j],arr[j + 1]=arr[j + 1],arr[j]
print arr

# 在Python当中用sort直接搞定
arr.sort()
print arr

li=range(10)
print li

