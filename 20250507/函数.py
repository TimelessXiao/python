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
