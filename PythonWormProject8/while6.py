while True:
    ch=0
    n = int(input("請輸入一個數值: "))
    total = 1
    i=1

    while i<=n:
        total *= i
        i += 1

    print(total)

    ch = int(input("請選擇(1)繼續執行(2)完全結束"))

    if(ch==2):
        break