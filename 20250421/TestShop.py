# 本案例要求编写代码，依次接收用户从键盘输入的商品价格，并根据价格输出购物小票内容
# 新建一个空字典
import time

a = float(input("请输入金士顿u盘的价格："))
b = float(input("请输入盛创16GTF卡的价格："))
c = float(input("请输入读卡器的价格："))
d = float(input("请输入网线2米的价格："))

arr = [
    ["金士顿u盘", 1, a, a],
    ["盛创16GTF卡", 1, b, b],
    ["读卡器", 1, c, c],
    ["网线2米", 1, d, d]
]
print("........................")
print("单号：DH" + time.strftime('%Y%m%d', time.localtime()) + "0001")
print("时间：" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
print("........................")
print("{:<10} {:<4} {:<10} {:<10}".format("名称", "数量", "单价", "金额"))
for v in arr:
    print("{:<8} {:<4} {:<10} {:<10}".format(v[0], v[1], v[2], v[3]))
print("........................")
print(f"总数：{arr[0][1] + arr[1][1] + arr[2][1] + arr[3][1]}",
      f"总额：{arr[0][3] + arr[1][3] + arr[2][3] + arr[3][3]:.2f}",
      sep="\t")
print("折后总额：%.2f" % (arr[0][3] + arr[1][3] + arr[2][3] + arr[3][3]))
print(f"实收：{arr[0][3] + arr[1][3] + arr[2][3] + arr[3][3]:.2f}",
      f"找零：{0.00}",
      sep="\t")
print("收银: 管理员")
