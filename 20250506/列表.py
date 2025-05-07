# 列表
# 直接使用 []
list1 = [1, 2, 3]
print(list1)
print(type(list1))

# 列表可以存放任意数据类型
list2 = [1, 2.1, [3, 3.1]]
print(type(list2))

# 使用list函数代表列表,存放的必须是可迭代对象，例如字符串，列表，元组
list3 = list([1, 2, 3, [1, 2, 3.3]])
print(type(list3))
# 元组改为列表
a = (1, 2, 3)
print(type(a))
list4 = list(a)
# 构造列表
print(type(list4))
print(list4)
# 字典改为列表
print(list({3, 4}))

# 列表的索引，访问列表元素,支持正向索引也可以反向索引，从0开始或-1开始
list5 = list("hello world")
print(list5)
print(list5[2])
# 正向索引
# 反向索引 -length ~ -1
print(list5[-len(list5)])

# 切片，得到一个子列表（相当于截取出一个列表）
# [开始:结束],开始包含，结束不包含
print(list5[0: len(list5)])
# [开始:结束:步长] 步长相当于加上跨越的数（下标）,默认步长是1
c = [1, 2, 3, 4, 5, 6]
# 0~6，从第一个数开始，跳过两个数 0 + 2 = 2，2 + 2 = 4，4 + 2 = 6
print(c[0:6:2])
print(c[0:6:3])

# 遍历
# 1.使用索引遍历
d = list("hello world")
for i in range(len(d)):
    print(d[i], end=" ")
# 2.遍历元素
for i in d:
    print(i, end=" ")
