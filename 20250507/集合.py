# 1.集合的创建
# 如果使用{}创建集合，必须里面添加内容，否则创建的是字典
a = {1}
print(type(a))
b = set()
print(type(b))
# [1,2,3]列表是可变的，所以不能添加，除列表以外集合和字典也是可变的，所以不能添加
# c = {1, 'a', [1, 2, 3], {"1": "2"}, {123}}
# c = {1, 'a', (1, 2, 3), {"1": "2"}, {123}}
# c = {1, 'a', (1, 2, 3), {123}}
c = {1, 'a', (1, 2, 3)}
print(c)

# set 函数的创建,作用是可以去重
d = set([1, 'a', (1, 2, 3)])
print(d)
e = set([1, 1, 2, 2])
print(e)

print("-----------")
# 2.集合的增删
f = set()
# 增
# 单增加
f.add(1)
f.add(2)
f.add(2)
print(f)
# 批量增加
f.update([1, 2, 3, 4, 5, 6, 5, 6])
print(f)

print("-----------")
# 删
f.remove(2)
print(f)
# 删除，如果有直接删，没有则不删，不报错
f.discard(2)
print(f)
# 随机删除，并返回一个值，空的集合会报错
g = f.pop()
print(g)
print(f)
print("--------")
#  清空
f.clear()
print(type(f))

print("-----------")
# 查
# 集合是无序的且不可重复的，如果要查只能用in或者not in 或者for循环遍历
print(1 in f)
print(2 not in f)
for i in f:
    print(i, end=" ")
print()
print("--------")
# 判断两个集合是否包含相同的元素，有返回True，没有返回False
print(f.isdisjoint({1, 2}))

print("-----------")
# 集合的推导式
h = {i for i in f if i % 2 == 0}
print(f)
print(h)
