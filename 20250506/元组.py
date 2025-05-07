# 元组
a = (1,)
print(type(a))
print(a)

b = (1, "2", 3.3, True)
print(b)

# tuple 将已存在的字符串，列表转换成元组
c = tuple("hello world")
d = tuple([1, 2, 3])
print(c)
print(d)

# 查询与切面
print(c[0])
print(c[-1])
print(c[0:len(c)])

# 元组推导式
e = tuple([1, 2, 3, 4, 5, 6])
f = tuple(i * 2 for i in e if i % 2 == 0)
print(f)
