mylist1 = [[10,20],[30, 40], [50, 60]]

leny =  len(mylist1)
lenx = len(mylist1[0])

for i in range(0, leny):
    for j in range(0, lenx):
        #print(i,j)
        print("mylist1[{0}][{1}]={2}".format(i,j ,mylist1[i][j]))



for k in range(0, leny):
    for h in range(0, lenx):
        print(mylist1[k][h], end="\t")


print()
for rowdata in mylist1:
    for data in rowdata:
        print(data, end="\t")
print()

for rowdata2 in mylist1:
    len2 = len(rowdata2)
    for r in range(0, len2, 1):
        print(rowdata2[r], end="\t")
