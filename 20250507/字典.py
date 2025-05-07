# 字典的创建
a = {}
b = {"name": "张三", "age": 18, "sex": "男", "hobby": ["足球", "篮球"], "address": {"province": "北京", "city": "北京"},
     "study": ("python", "java")}
print(type(a))
print(type(b))
print(b)

# 使用dict函数进行创建
c = dict()
print(type(c))

print("------------")
# 字典的增删改查
# 修改和添加，存在则修改，不存在则添加
b.update({"name": "李四", "age": 19})
b.update({"aaa": "1111"})
print(b)
b["name"] = "王五"
b["5555"] = "66666"
print(b)
b.update(name="赵六")
b.update(ssss=999999)
print(b)

print("------------")
# 删
del b["name"]
print(b)
# 删除并返回对应的值
d = b.pop("aaa")
print(d)
print(b)
# 随机删除
e = b.popitem()
print(e)
print(b)
# 清空
# b.clear()

print("------------")
# 查
print(b["age"])
print(b.keys())
print(b.values())
print(b.items())

for i in b.items():
    print(f"{i[0]}  {i[1]}")

for k, v in b.items():
    print(f"{k}  {v}")

print("------------")
# 字典的推导式
y = {k: v for k, v in b.items() if k == "age"}
print(y)
