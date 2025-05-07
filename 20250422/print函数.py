#print函数括号中可以放多个参数，他们之间使用 “，”隔开
a=1
b=2
print(a,b)
#print函数多个参数输出时，参数与参数之间默认是空格，可以使用sep参数修改默认空格
print(a,b,sep="-")
print(a,b,sep=" ")
#print函数输出时，两个输出函数输出时默认输出结尾是换行，可以使用end参数修改默认换行
print(a,b,end="-------")
print(a,b,end="\n")


print(a,b,sep="-",end="*******")
print(a,b,sep=" ",end="\n")