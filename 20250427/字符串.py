# 定义字符串有三种方式，1.使用单引号，2.使用双引号，3.使用三引号
print("hello world")
print('hello world')
print('''hello 
         world''')

# 将引号" ' "作为字符串输出
# 方式一：直接写
print("hello 'world' ")
# 方式二：使用转义字符 \加上一个特殊字符这样的组合就是转义字符
print("hello \'world\' ")

# \b 回退符，打印输出时 光标在最后一位，退格符的作用从\b也就是光标的位置往前删除一个
print("hello world\b")

# 输出字符串的长度，空格算一个字符，转义字符也算一个字符，使用的是len()函数
print(len("hello world\b"))

# \n 换行符
print("hello\nworld")

# \r 回车符，覆盖\r之前的内容
print("hello\rworld")

# 将转义字符作为内容输出
print(r"hello\rworld")
