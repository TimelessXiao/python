#  根据用户输入的昵称和植物名字生成一个证书
import time

name = input("请输入你的昵称：")
plant = input("请输入你的植物名字：")
print("{:^30}".format("植物证书"))
print("-----------------------------------")
print(f"{name}", "谢谢你:")
print(f"  你申请种植的 {plant} ,将由伊利\n公益基金会负责种下。查看种植进程>")
print()
print("树苗编号: NO.HBI66308960305")
print("申请时间:", "%s" % (time.strftime('%Y年%m月%d日', time.localtime())))
