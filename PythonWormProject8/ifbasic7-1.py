
try:
    month = int(input("請輸入月份: "))
    if month >= 1 and month <=3:
        print("%d 月是春天" % month)

    #month >= 4 and
    elif month <=6:
        print("%d 月是夏天"  % month )

    #month >= 7 and
    elif month <=9:
        print("%d 月是秋天" % month )

    elif month <=12:
        print("%d 月是冬天" % month)

except:
    print("資料格式錯誤")
