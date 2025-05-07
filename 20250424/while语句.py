# 计算1+...+100
i = 1
total = 0
while i < 101:
    total = total + i
    i = i + 1
print(total)

# fro in 循环
# range 控制循环次数，如果有两个参数，遵循闭开原则，例如（1,101）执行1开始到100，不包括101
# 如果只有一个参数，那么就是从0开始到指定数字，不包括指定数字
total = 0
for i in range(1, 101):
    total += i

print(total)

arr = [1, 3, 5, 7, 9]
# 打印集合的下标（索引）
for n in range(len(arr)):
    print(n)
# 打印集合的值
for n in range(len(arr)):
    print(arr[n])
# 直接访问元素，n是循环中的临时变量，代表序列中的每一个元素，相当于增强for循环
for n in arr:
    print(n)
