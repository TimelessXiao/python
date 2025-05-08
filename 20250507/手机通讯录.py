#  手机通讯录记录了联系人的联系方式和基本信息，
#  人们在手机通讯录中通过姓名可以方便查看相关联系人的手机号、电子邮箱、联系地址等信息，也可以自由编辑联系人信息，包括新增、修改、删除联系人等。
#  通讯录通常包含6个功能，每个功能都对应一个序号，用户选择序号执行相应的操作。手机通讯录中各功能的介绍如下。
# （1）添加联系人：用户根据提示分别输入联系人的姓名、手机号、电子邮箱和联系地址，输入完成后输出保存成功的提示信息。注意，若输入的用户信息为空，会提示用户输入的正确信息。
# （2）查看通讯录：如果通讯录不为空，按照固定的格式展示通讯录中每个联系人的信息。如果通讯录为空，则会直接提示通讯录无信息。
# （3）删除联系人：如果通讯录不为空，则用户根据提示输入联系人的姓名，若该联系人在通讯录中，则删除该联系人，提示删除成功，否则提示该联系人不在通讯录中。如果通讯录为空，则会直接提示通讯录无信息。
# （4）修改联系人：如果通讯录不为空，用户根据提示输入要修改联系人的姓名，之后按照提示分别输入该联系人的新姓名、新手机号、新电子邮箱、新联系地址，并输出修改成功的提示信息。如果通讯录为空，则会直接提示通讯录无信息。
# （5）查找联系人：如果通讯录不为空，用户根据提示输入联系人的姓名，若该联系人存在于通讯录中，则输出该联系人的所有信息，否则输出该联系人不在通讯录中的提示信息。如果通讯录为空，则会直接提示通讯录无信息。
# （6）退出：退出手机通讯录。如果用户不主动选择退出，那么可以一直使用手机通讯录。
# 本案例要求编写程序，实现具有如上功能的手机通讯录。

person_list = {
    '张三': {
        'phone': '12345678901',
        'email': '123@qq.com',
        'address': '湖北'
    },
    '李四': {
        'phone': '12345678902',
        'email': '123@qq.com',
        'address': '北京'
    },
    '王五': {
        'phone': '12345678903',
        'email': '123@qq.com',
        'address': '上海'
    }

}
while True:
    i = input('''
    请选择以下功能：
    1.添加联系人
    2.查看通讯录
    3.删除联系人
    4.修改联系人
    5.查找联系人
    6.退出
    ''')
    if i == '1':
        name = input('请输入联系人姓名：')
        phone = input('请输入联系人手机号：')
        email = input('请输入联系人邮箱：')
        address = input('请输入联系人地址：')
        person_list[name] = {
            'phone': phone,
            'email': email,
            'address': address
        }
        print('保存成功！')
        continue
    elif i == '2':
        if person_list:
            for k, v in person_list.items():
                print('姓名：%s 手机号：%s 邮箱：%s 地址：%s' % (k, v['phone'], v['email'], v['address']))
        else:
            print('通讯录无信息！')
        continue
    elif i == '3':
        name = input('请输入要删除的联系人姓名：')
        if name in person_list:
            del person_list[name]
            print('删除成功！')
        else:
            print('该联系人不在通讯录中！')
    elif i == '4':
        name = input('请输入要修改的联系人姓名：')
        if name in person_list:
            phone = input('请输入联系人手机号：')
            email = input('请输入联系人邮箱：')
            address = input('请输入联系人地址：')
            person_list[name] = {
                'phone': phone,
                'email': email,
                'address': address
            }
    elif i == '5':
        name = input('请输入要查找的联系人姓名：')
        if name in person_list:
            print('姓名：%s 手机号：%s 邮箱：%s 地址：%s' % (name, person_list[name]['phone'], person_list[name]['email'],
                                                         person_list[name]['address']))
        else:
            print('该联系人不在通讯录中！')
    elif i == '6':
        print('退出成功！')
        break
    else:
        print('请输入正确的序号！')
