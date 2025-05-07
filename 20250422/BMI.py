# 根据输入的体重和身高测算BMI
weight = float(input("请输入体重(kg)："))
height = float(input("请输入身高(m)："))
bmi = weight / (height * height)
print("您的BMI指数为：", bmi)
