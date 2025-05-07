"""print("hello world")
print("123")
if True:
    print("true")
    print("在同一代码块中，缩进要保持相同")
else:
    print("false")
    print("在else代码块中")


a = 1

print(type(a))

user_name = input("请输入账户名:")
user_password = input("请输入密码:")
print("账户名："+user_name)
print("密码："+user_password)
"""

#列表，使用[]表示，可以存放任意数据类型，任意数量的元素，可以后期增减
a = [1,3.5,"娃哈哈",True]
print(a[0]) #正向索引，从0开始

print(a[-4])#反向索引，从-1开始，指向的是列表最后一个元素，然后往前推

a.append("增加了一个元素")#在列表的的最后增加一个元素

a.pop(1)#根据索引删除一个元素，下标为1，也就是第二个元素“3.5”

print(a[0:3])#根据索引截取元素，从索引 0 开始，取到索引 3 之前（不包括索引 3）

print(a[0:-1])#根据索引截取元素，从索引 0 开始，取到索引 倒数第一个 之前（不包括索引倒数第一个）

del a[0] #根据索引删除列表中的数据

print(a)


    