# 增加元素
# append方法,在尾部添加任意元素
str1 = list("hello world")
str1.append(1)
str1.append(2)
str1.append(3)
str1.append([4, 5, 6])
str1.append("-你好，世界")
print(str1)

# extend方法，在尾部添加任意序列数据（列表，元组，字符串）也就是可迭代对象，其它的数据类型不行，添加的是序列数据展开的元素
str2 = list("hello world")
str2.extend([2, 3, 4])
str2.extend("-你好，世界")
print(str2)

# insert方法，需要提供添加的索引和元素
str3 = list("hello world")
str3.insert(0, 1)
str3.insert(1, [2, 3])
print(str3)

# 删除
# del方法，可以删除指定的元素，也可以将整个列表删除,删除后str4不存在
str4 = list("hello world")
del str4[0]
print(str4)
del str4

# remove方法,删除指定的元素
str5 = list("hello world")
str5.remove("h")
print(str5)

# pop方法,参数默认是最后一个元素，也可以指定删除下标元素
str6 = list("hello world")
str6.pop()
print(str6)
str6.pop(1)
print(str6)

# clear 方法，直接将列表清空
str7 = list("hello world")
str7.clear()
print(str7)

# 修改
str8 = list("hello world")
str8[0] = "a"
print(str7)
