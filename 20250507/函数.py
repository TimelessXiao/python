# 函数的定义
def fun1():
    print("hello world")


# 函数的调用
fun1()

print("-----" * 20)


# 方法可以重新被定义
def fun1():
    print("hello python")


fun1()


# 带参数和返回值的函数
def add(a, b):
    print("a=", a, "b=", b)
    return a + b


# 参数必须要传递，但是类型不限制
# 位置参数传递
print(add(1, 2))
print(add("a", "b"))
# 关键字参数传递
print(add(b=2, a=3))


# 默认参数的定义和传递
def fun2(a, b=10):
    print("a=", a, "b=", b)


fun2(10)
fun2(10, 30)
fun2(b=20, a=10)


# 仅限位置
# a: 第一个位置参数，必须通过位置传入。
# b: 第二个位置参数，同样必须通过位置传入。
# [/]: 这是一个符号性参数，表示其前面的参数只能以位置方式传入。
# c: 可以通过位置或关键字传入。
def fun3(a, b, /, c):
    print("a=", a, "b=", b, "c=", c)


fun3(10, 20, 30)
fun3(10, 20, c=30)


# 参数的打包和解包
# 传递的参数会以元组形式传递给函数
# 元组的变量名称通常为 args
# 元组在参数中只能定义一次 def fun4(*args,*a)是错误的写法
def fun4(*args):
    print(args)


fun4(1, 2, 3, 4)
fun4(1, 1, 1)
