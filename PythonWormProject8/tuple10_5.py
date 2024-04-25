data = [    ("p1001" , "小明" ,60, 70, 80),
            ("p1002" , "小玲" ,70, 50, 90),
            ("p1003" , "小童" ,23, 60, 80),
            ("p1004" , "小張" ,93, 60, 90),
            ("p1005" , "小巾" ,70, 56, 86)
        ]
leny = len(data)


for i in range(0, leny):
    mydata=data[i]
    lenx = len(mydata)
    for j in range(0, lenx):
        print(mydata[j], end='\t')
    print()