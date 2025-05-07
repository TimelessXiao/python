# 1.编写程序，实现利用while循环输出100以内偶数的功能。
from itertools import count

i = 1
while i < 101:
    if i % 2 == 0:
        print(i)
    i += 1

# 2.编写程序，实现判断用户输入的数是正数还是负数的功能。
num = int(input("请输入一个整数："))
if num > 0:
    print("是正数")
elif num < 0:
    print("是负数")
else:
    print("您输入的是 0")

# 3.编写程序，实现输出100以内质数的功能。
i = 1
while i < 101:
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)
    i += 1

# 4.编写程序，已知字符串s = 'AbcDeFGhIJ'，请计算该字符串中小写字母的数量。
s = 'AbcDeFGhIJ'
count = 0
for i in s:
    if i == i.lower():
        count += 1
print(count)

# 5.编写程序，检查字符串" Life is short. I use python"中是否包含字符串"python"，若包含则替换
#   为"Python"后输出新字符串，否则输出原字符串。
s = "Life is short. I use python"
if s.find("python") == -1:
    print(s)
else:
    print(s.replace("python", "Python"))

    # 6.文字排版工具是一款强大的文章自动排版工具，它会将文字按现代汉语习惯及发表出版要求进行规范编
    # 排。编写代码，实现一个简易版的中文文字排版工具，具体要求如下。
    # 1. 用户开始使用时会看到欢迎的提示信息，并输入要排版的文字。
    # 2. 文字排版工具一共有5个功能，分别是删除空格（编号1）、英文标点替换（编号2）、段落分割
    # （编号3）、字母大写（编号4）和退出（编号0），用户可以输入编号选择相应的功能。关于各功
    # 能的介绍如下。
    # 删除空格：删除文字里面的任意位置的空格。
    # 英文标点替换：将文字里面的英文逗号、句号、问号、感叹号、冒号替换为中文逗号、句号、
    # 问号、感叹号、冒号。
    # 段落分割：将文字里面的\r\n作为段落标记以多段内容进行显示。
    # 字母大写：将文字里面的英文字母全部转换为大写形式的英文字母。
    # 退出：输出感谢使用的提示信息，并退出文字排版工具。注意，如果用户没有选择退出功能，
    # 则可以一直使用文字排版工具。
    # 3. 提供功能菜单，便于用户根据菜单的提示选择想要的功能。如果用户输入了错误的编号，则会输出
    # 无效选项的提示信息。

    text = input("欢迎进入文字排版系统，请输入要排版的文字：")
while True:
    select = input("请选择功能：\n1. 删除空格\n2. 英文标点替换\n3. 段落分割\n4. 字母大写\n0. 退出\n")
    if select == '1':
        text = text.replace(" ", "")
        print("删除空格完毕：", text)
    elif select == '2':
        text = (text.replace(",", "，")
                .replace(".", "。")
                .replace("?", "？")
                .replace("!", "！")
                .replace(":", "："))
        print("英文标点符号替换完毕：", text)
    elif select == '3':
        paragraph = text.split(r"\r\n")
        print("段落分割完毕：")
        for i in paragraph:
            print(i)
    elif select == '4':
        text = text.upper()
        print("字母大写完毕：", text)
    elif select == '0':
        print("已退出")
        break
    else:
        print("无效选项")
