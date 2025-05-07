# 算术运算符 + - * / % // **
a = 10
b = 3
print(a + b)
print(a - b)
print(a * b)
# 除法运算符 /，返回浮点数
print(a / b)
# 除法运算符 //，返回整数
print(a // b)
# 取余运算符 %，返回余数
print(a % b)
# 幂运算符 **，返回a的b次幂
print(a ** b)

print(".....................")
# 逻辑运算符 and(与) or(或) not(非)
# and(与)逻辑运算符，如果两个条件都为真，则返回真（右边的值），否则返回假（一真一假返回假的那个值，全假返回左边的值）
a = 10
b = 20
c = 0
d = False
print(a and b)
print(a and c)
print(d and c)

print(".....................")
# or(或)逻辑运算符，如果左边条件为真，则返回真（左边的值），否则返回假（右边的值）
print(a or b)
print(a or c)
print(c or a)
print(c or d)

print(".....................")
# nor(非)逻辑运算符，参数为真时返回假，为假时返回真
print(not a)
print(not d)

# 成员运算符,成员存在返回true，不存在返回false
a = ["leman", 123, True]
b = "leman"
print(b in a)
print(b not in a)
