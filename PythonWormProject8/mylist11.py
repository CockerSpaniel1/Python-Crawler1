while True:
    a = [10,20, 30 ,40 ,50]
    len1 = len(a)
    qdata = input("請輸入欲查詢資料:")
    x = False

    for i in range(0, len1):
        if int(qdata) == a[i]:
            x = True
            break


    if x == True:
        print("[%s]資料存在資料來源中" % qdata)
    else:
        print("[%s]資料不存在資料來源中" % qdata)

    ch = input("menu(1)重新執行(2)完全結束")
    if int(ch)==2:
        break

