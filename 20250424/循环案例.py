import time

i = 3

"""while i > 0:
    username = input("请输入用户名：")
    password = input("请输入密码：")
    if username == "admin" and password == "123456":
        print("登录成功")
        break
    else:
        print("用户名或密码错误，请重新输入")
        i -= 1
        print("您还有", i, "次机会")
        if i == 0:
            print("登录失败")
            time.sleep(3)
            i = 3

"""
"""a = 1
while a < 10:
    print("*" * a)
    a += 1

for i in range(3):
    for j in range(i + 1):
        print("*", end=" ")
    print()

print("------")
for i in range(3):
    for j in range(3 - i):
        print("*", end=" ")
    print()

print("------")
for i in range(3):
    for j in range(i):
        print(" ", end=" ")
    for j in range(3 - i):
        print("*", end=" ")
    print()

print("------")
for i in range(3):
    for j in range(3 - i - 1):
        print(" ", end=" ")
    for q in range(i + 1):
        print("*", end=" ")
    print()

print("------")
for i in range(10):
    for j in range(10):
        print("+", end=" ")
    print()
"""
while True:
    select = input("请输入您的贷款类型：01（商业贷款），02（公积金贷款），exit（退出）：")
    if select != "01" and select != "02" and select != "exit":
        print("输入有误，请重新输入")
        continue
    if select == "exit":
        print("退出成功")
        break
    a = int(input("请输入您的贷款周期(年)："))
    b = float(input("请输入您的贷款金额(万元)："))
    if select == "01":
        if a <= 5:
            rate = 0.0475 / 12
        else:
            rate = 0.0490 / 12
    elif select == "02":
        if a <= 5:
            rate = 0.0260 / 12
        else:
            rate = 0.0310 / 12
    price = b * (rate * (1 + rate) ** (a * 12) / ((1 + rate) ** (a * 12) - 1))
    total_price = price * a * 12
    lixi = total_price - b
    print(f"您的月供为：{price:.3f}万元")
    print(f"您的还款总额为：{total_price:.3f}万元")
    print(f"您的支付利息为：{lixi:.3f}万元")
