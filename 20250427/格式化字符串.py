# 将一个字符串作为变量
# 方法一：直接拼接
str = "湖北宜昌"
print("这里是：", str)

# 方法二：格式化字符串,%, %d表示数字类型（十进制），%s表示字符串类型，%f表示浮点数类型
# %c表示字符类型，%.2f表示保留两位小数，%o表示八进制，%x表示十六进制，%b表示二进制
sql = "select * from user where id = %d"
print("sql语句：", sql % 1)

sql = "select * from user where id = %d and name = %s and price = %.1f"
print("sql语句：", sql % (1, "张三", 12.3))

# %d可以表示一个整数的占位符，在%d中可以指定位数，指定位数>实际位数不变化，指定位数<实际位数，默认前面补空格，也可以指定使用0来填充
print("整数格式为：%2d" % 123)
print("整数格式为：%4d" % 123)
print("整数格式为：%04d" % 123)

# 方法三：format方法，{}表示占位符，
sql = "select * from user where id = {} and name = {} and price = {}"
print("sql语句：", sql.format(1, "张三", 12.3))

# {}中可以输出指定参数的位置的数,但是计数是从0开始，从左到右,不写默认是0,要么不指定，要么全都指定位置，也可以指定名称
print("这是一条数据：{},第二条数据是：{},第三条数据是：{}".format("123", "hello world", 456))
print("这是一条数据：{0}".format("123", "hello world", 456))
print("这是一条数据：{2}".format("123", "hello world", 456))
print("这是一条数据：{a1},第二条数据是：{a2},第三条数据是：{a3}".format(a1="123", a2="hello world", a3=456))

# 可以指定位数
print("整数格式为：{:.2f}".format(0.123))

# 方式四：f-string
id = 1
name = "张三"
price = 12.3
print(f"sql语句：select * from user where id = {id} and name = {name} and price = {price:.02f}")
