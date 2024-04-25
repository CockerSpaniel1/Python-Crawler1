try:
    try:
        a = input("數值1:")
        b = input("數值2:")
        sum = int(a)/int(b)
        print(sum)

    except NameError:
        print("使用沒有被定義的對象")
    except ZeroDivisionError:
        print("不可以除0")

except:
    print("型別發生錯誤")

