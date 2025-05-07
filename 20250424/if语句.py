# 实践练习
price = int(input("请输入您消费的金额:"))
points = int(input("请输入您的积分:"))
"""if price >= 1000 and points >= 10000:
    print("您的会员等级为 钻石会员")
elif 500 <= price < 1000 and 2000 <= points < 5000:
    print("您的会员等级为 白金会员")
elif price >= 200 and points > 2000:
    print("您的会员等级为 黄金会员")
elif price >= 100 and points >= 1000:
    print("您的会员等级为 白银会员")
elif points >= 500:
    print("您的会员等级为 青铜会员")
else:
    print("您的会员等级为 普通会员")"""

# 三元运算符
a = "您的会员等级为 钻石会员" if price >= 1000 and points >= 10000 else \
    "您的会员等级为 白金会员" if price >= 500 and points >= 2000 else \
        "您的会员等级为 黄金会员"
