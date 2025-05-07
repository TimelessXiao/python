# find方法 find()
str = "hello world"
# 找到就输出字符串的下标（如果有多个就输出第一个找到的字符的下标），如果没有找到就返回-1
print(str.find("w"))
print(str.find("o"))
print(str.find("11111"))

# 可以指定区间来查，开始(下标)(包含)(可以不写，默认从下标0开始查) - 结束(下标)(不包含)(可以不写，默认一致查找到最后)
print(str.find("o", 0, 5))
# 实行左闭右开原则，0下标可以查找，4下标不可以查
print(str.find("o", 0, 4))
print(str.find("o", 5))

print("----------")
# 字符串替换
str = "h ell o wor ld"
print(str.replace(" ", ""))
print(str.replace("h", "H"))

print("----------")
# 字符串分割
src = "D:/Telegram/Telegram Desktop"
# 将字母e作为分隔符，分割字符串，返回一个列表
src1 = src.split('e')
print(type(src1))
print(src1)

print("----------")
# 字符串连接
# 将字母e作为连接符，将列表src1连接成字符串，返回字符串
print('e'.join(src1))

print("----------")
# 删除指定的字符串中的字符
str = " hello world"
# 1.strip 删除字符串两端的字符，默认删除空格
print(str)
print(str.strip())
# lstrip 删除字符串左侧的字符，默认删除空格
str = "hello world"
print(str.lstrip("h"))
# rstrip 删除字符串右侧的字符，默认删除空格
str = "hello world"
print(str.rstrip("d"))

print("----------")
# 字母大小写转换
str = "hello world"
# 转大写
print(str.upper())
# 转小写
print(str.lower())
# 第一个字母大写，其他字母小写
print(str.capitalize())
# 单词的首字母大写，其它字母小写
print(str.title())

print("----------")
# 字符串对齐
str = "hello world"
# 居中对齐，字符串总长度30字符，输出时两边填充字符为*
print(str.center(30, "*"))
# 左对齐，字符串总长度30字符，输出时两边填充字符为*
print(str.ljust(30, "*"))
# 右对齐，字符串总长度30字符，输出时两边填充字符为*
print(str.rjust(30, "*"))

print("----------")
# 切片
str = "hello world"
# 通过索引取值，索引从0开始，从length-1结束(也可以反向取值)
print(str[0])
print(str[len(str) - 1])
# 反向取值，最后一个字符是开始是-1 ，-length是第一个字符的位置
print(str[-1])
print(str[-len(str)])
# 取值范围，使用左闭右开原则,0是默认的，可以不用写，最后一个也是默认的可以不用写
print(str[0:len(str)])
print(str[:5])
print(str[:])
print(str[-3:])
