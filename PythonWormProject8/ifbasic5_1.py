ch = input("Menu(1)Led1 on (2)Led2 on(3)Led3 on(4)All Led on(5)All Led off:")

xlen = len(ch)

if xlen==0:
    print("%s" % "變數不可以為空值")
else:
    ch = int(ch)
    if (ch>=1 and ch <=5):
        if ch==1:
            print("燈號一亮")
        elif ch==2:
            print("燈號二亮")
        elif ch==3:
            print("燈號三亮")
        elif ch==4:
            print("燈號全亮")
        elif ch==5:
            print("燈號全暗")
    else:
        print("只能輸入1-5範圍值")