mylist1 = []

mylist1.append("java")
mylist1.append("javascript")
mylist1.append("delphi")
mylist1.append("c++")
mylist1.append("jquery")


while True:
    ch = input("menu(1)新增資料(2)瀏覽資料(3)結束")
    if ch == "1":
        x = input("輸入資料")
        mylist1.append(x)

    if ch == "2":
        for i in mylist1:
            print(i)

    if int(ch) == "3":
        break