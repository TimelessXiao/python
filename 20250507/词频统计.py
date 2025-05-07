#  词频统计是一种统计文本中单词出现频率的方法，它可以帮助我们了解文本中哪些单词出
#  现得最频繁，或者在某个特定的上下文中，某些单词的使用情况。本案例要求根据用户输
#  入的一段英文内容，将这部分内容转为小写后统计并输出每个单词的出现次数。
my_str = input("请输入纯英文内容：")
# 将各种符号和空格都去掉
my_str = (my_str.replace(",", "")
          .replace(".", "")
          .replace("?", "")
          .replace("!", "")
          .replace(":", "")
          .replace(" ", ""))
# 转小写
lower_str = my_str.lower()
# 去重
remove_str = set(lower_str)
# 排序
remove_str = list(remove_str)
remove_str.sort()
# 将数据放入字典中
dic = {}
for i in remove_str:
    dic.update({i: lower_str.count(i)})
print(dic)
