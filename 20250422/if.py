# if选择语句，执行顺序是从上到下，直到找到一个条件为真的语句，然后执行该语句，并结束。
# 有if ， if...else ， if...elif...else 三种情况
age = 20
if age >= 18:
    print('已经成年了')
elif age >= 6:
    print('青少年')
else:
    print('儿童')

#  三目运算符
# 值1 if 条件 else 值2  如果条件成立执行值1，否则执行值2
age = 12
print("我已经成年了" if age >= 18 else "我还是青少年")

# 课程实践
price = int(input("请输入您消费的金额:"))
points = int(input("请输入您的积分:"))
if price >= 1000 and points >= 10000:
    print("您的会员等级为 钻石会员")
elif price >= 500 and points >= 5000:
    print("您的会员等级为 白金会员")
elif price >= 200 and points >= 2000:
    print("您的会员等级为 黄金会员")
elif price >= 100 and points >= 1000:
    print("您的会员等级为 白银会员")
elif points >= 500:
    print("您的会员等级为 青铜会员")
else:
    print("您的会员等级为 普通会员")

# 课程实践
address = input("请输入您想要邮寄的地区编号:")
weight = float(input("请输入您想要邮寄的包裹重量(kg):"))
if address == "01":
    if weight <= 2:
        print("您的运费为：%d元" % 13)
    else:
        print("您的运费为：%d元" % (13 + (weight - 2) * 3))
elif address == "02":
    if weight <= 2:
        print("您的运费为：%d元" % 12)
    else:
        print("您的运费为：%d元" % (12 + (weight - 2) * 2))
else:
    if weight <= 2:
        print("您的运费为：%d元" % 14)
    else:
        print("您的运费为：%d元" % (14 + (weight - 2) * 4))
