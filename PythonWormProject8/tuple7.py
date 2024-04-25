tup1 = (12, 67, 88 ,32 ,11)
mylist2 = list(tup1)
del mylist2[2]
tup1 = tuple(mylist2)

len1= len(tup1)

for i in range(0, len1):
    print(tup1[i])