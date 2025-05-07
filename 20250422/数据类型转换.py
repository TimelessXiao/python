# 两个不同数据类型进行运算时需要数据类型转换
# 可以使用函数进行数据类型转换
# int() float() str()函数
a = 1
b = 1.2
c = '3'
d = True
e = 0b10001
# int类型转换
print(a + b)
print(a + int(c))
print(a + int(d))
print(a + int(e))

# float类型转换
print(a + float(c))

# str类型转换
print(type(str(b)))

# complex类型转换
print(complex(a, int(b)))
# 如果是字符串，运算符不能有空格
print(complex("1+2j"))
