# 获取当前时间戳
import time

nowTime = time.localtime(time.time())
while True:
    country = input("请输入想要转换的国家时间格式：01(中国),02(美国),exit(退出)：")
    year = nowTime.tm_year
    month = nowTime.tm_mon
    day = nowTime.tm_mday
    hour = nowTime.tm_hour
    minute = nowTime.tm_min
    second = nowTime.tm_sec
    if country == "01":
        print(f"{year}年{month:02d}月{day:02d}日 {hour:02d}:{minute:02d}:{second:02d}")
    elif country == "02":
        print(f"{month:02d}/{day:02d}/{year} {hour:02d}:{minute:02d}:{second:02d}")
    elif country == "exit":
        print("您已退出！")
        break
    else:
        print("您输入的格式有误，请重新输入！")
