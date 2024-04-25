chi = input("(1)春天(2)夏天(3)秋天(4)冬天: ")

if chi!="":
    chi = int(chi)
    if chi>= 1 and chi <=4:
        if chi==1:
            print("櫻花")
        elif chi==2:
            print("金針花")
        elif chi==3:
            print("楓葉")
        elif chi==4:
            print("梅花")
    else:
        print("只能輸入1-4項目")

else:
    print("請選擇項目")
