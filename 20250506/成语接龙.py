a = ["万事如意", "发愤图强", "笑容满面", "笑容满面", "意气风发", "强颜欢笑"]
str_start = a[0][0]
str_end = a[0][3]
b = ["万事如意"]
for j in range(len(a)):
    for i in range(len(a)):
        if str_end == a[i][0]:
            b.append(a[i])
            str_start = a[i][0]
            str_end = a[i][3]
print(b)
