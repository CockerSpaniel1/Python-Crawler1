mylist = []
data = []

for k in range(1, 9+1, 1):
    r = int(input("輸入第("+str(k)+")元素:"))
    if k%3 ==0:
        data.append(r)
        mylist.append(data)
        data = []
    else:
        data.append(r)

print(mylist)
print()

leny = len(mylist)
lenx = len(mylist[0])

for i in range(0, leny):
    for j in range(0, lenx):

        print("mylist[{0}][{1}]=[{2}]".format(i, j ,mylist[i][j]))