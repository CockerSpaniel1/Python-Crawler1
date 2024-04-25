print(10,20,30, sep="-", end=" ") #不換行輸出

print(40,50,60,sep="*")

'''
Python
各種輸出
print()
'''

print("我的年齡:%d" %  45)
print("姓名:%s 學歷:%s 薪資:%d萬" % ("古力娜札","碩士",12))
print("血型:%c" % "A" )
print("現在溫度:%f " % 35.676)
print("現在溫度:%.2f " % 35.676)
print("現在溫度:%8.2f " % 35.676)

import math
print("現在溫度:%.0f " % math.floor(35.676))
print("現在溫度:%.0f " % math.ceil(35.676))
print("現在溫度:%.0f " % round(35.676))
print("現在溫度:%.0f " % round(35.676, 2))