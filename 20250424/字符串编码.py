# 字符串编码的作用就是将语言文字转换为计算机理解的二进制数据
# 可以使用不同的编码方式表示同一种语言，例如中文可以使用GBK编码，也可以使用UTF-8编码表示

# Unicode 编码


a = "hello world"
print(a, type(a.encode()), sep="\n")
