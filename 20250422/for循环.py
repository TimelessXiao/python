# for循环语句
import time

for world in "hello world":
    print(world, end=" ")
print("-------")
# for循环语句经常和range()函数一起使用
for i in range(10):
    print(i, end=" ")

print("-------")
for i in range(1, 10):
    print(i, end=" ")

print("-------")
for i in range(1, 10, 2):
    print(i, end=" ")

print("-------")
""" 
i = 1
n = 3
while i:
    # 实践练习
  username = input("请输入用户名：")
    password = input("请输入密码：")
    if username == "admin" and password == "123456":
        print("登录成功")
        i = 0
    else:
        print("用户名或者密码错误")
        n = n - 1
        print("您还有%d次机会" % n)
        if n == 0:
            print("输入次数过多，请稍后再试")
            time.sleep(10)

"""
for i in range(10):
    for j in range(10):
        print(".", end=" ")
    print()

# 实践练习
while True:
    dai_kuan_type = input("请输入您的贷款类型（商业贷款01，公积金贷款02）：")
    if dai_kuan_type != "01" and dai_kuan_type != "02" and dai_kuan_type != 'exit':
        print("输入有误，请重新输入")
        continue
    if dai_kuan_type == 'exit':
        print("退出程序")
        break
    year = int(input("请输入贷款年限（年）："))
    price = int(input("请输入贷款金额（万元）："))
    if dai_kuan_type == "01":
        if year <= 5:
            rate = 0.0475
            monthly_payment = price * rate * (1 + rate) ** (year * 12) / ((1 + rate) ** (year * 12) - 1) * 10000
            print(f"每月月供为：{monthly_payment:.0f}元")
            print(f"还款总额为：{monthly_payment * year * 12:.0f}元")
            print(f"利息总额为：{monthly_payment * year * 12 - price * 10000:.0f}元")
        else:
            rate = 0.0490
            monthly_payment = price * rate * (1 + rate) ** (year * 12) / ((1 + rate) ** (year * 12) - 1) * 10000
            print(f"每月月供为：{monthly_payment:.0f}元")
            print(f"还款总额为：{monthly_payment * year * 12:.0f}元")
            print(f"利息总额为：{monthly_payment * year * 12 - price * 10000:.0f}元")
    elif dai_kuan_type == "02":
        if year <= 5:
            rate = 0.026
            monthly_payment = price * rate * (1 + rate) ** (year * 12) / ((1 + rate) ** (year * 12) - 1) * 10000
            print(f"每月月供为：{monthly_payment:.0f}元")
            print(f"还款总额为：{monthly_payment * year * 12:.0f}元")
            print(f"利息总额为：{monthly_payment * year * 12 - price * 10000:.0f}元")
        else:
            rate = 0.0031
            monthly_payment = price * rate * (1 + rate) ** (year * 12) / ((1 + rate) ** (year * 12) - 1) * 10000
            print(f"每月月供为：{monthly_payment:.0f}元")
            print(f"还款总额为：{monthly_payment * year * 12:.0f}元")
            print(f"利息总额为：{monthly_payment * year * 12 - price * 10000:.0f}元")
