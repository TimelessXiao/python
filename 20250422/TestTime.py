#  根据用户输入的起始时间和结束时间，计算时间间隔使用的是24小时制，返回小时分钟
hour = int(input("请输入起始时间小时数："))
minute = int(input("请输入起始时间分钟数："))
end_hour = int(input("请输入结束时间小时数："))
end_minute = int(input("请输入结束时间分钟数："))

if (end_hour > hour):
    interval_hour = end_hour - hour
else:
    interval_hour = end_hour - hour + 24

if (end_minute > minute):
    interval_minute = end_minute - minute
else:
    interval_minute = end_minute - minute + 60
    interval_hour -= 1

print("时间间隔为：", interval_hour, "小时", interval_minute, "分钟")

start_minute = hour * 60 + minute
end_minute = end_hour * 60 + end_minute
interval_minute = end_minute - start_minute
interval_hour = interval_minute // 60
interval_minute = interval_minute % 60
print("时间间隔为：", interval_hour, "小时", interval_minute, "分钟")
