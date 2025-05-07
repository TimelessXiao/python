# 例子：快速得到0~10之间偶数集的列表 0,2,4,6,8
a = [0, 2, 4, 6, 8]
b = [i for i in a]
print(b)
c = [i for i in range(0, 10) if i % 2 == 0]
print(c)
d = [i * 2 for i in range(0, 10) if i % 2 == 0]
print(d)
