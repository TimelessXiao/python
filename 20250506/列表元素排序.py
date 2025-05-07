# sort方法排序,默认升序，相当于a.sort(key = None,reverse = False)
str1 = [1, 5, 2, 4, 3, 6, 9, 7, 8, 10]
str1.sort()
print(str1)
# 降序
str1.sort(reverse=True)
print(str1)

# sorted方法，将列表进行升序排序，返回一个新的列表，不会改变原列表
str2 = [1, 5, 2, 4, 3, 6, 9, 7, 8, 10]
str3 = sorted(str2)
print(str2)
print(str3)

# reverse方法，将列表翻转
str4 = list("hello world")
str4.reverse()
print(str4)
