tup1 = (12, 67 , 88 ,32, 11)

print(tup1[0])
print(tup1[1])
print(tup1[2])
print(tup1[3])
print(tup1[4])

len1 = len(tup1)

for i in range(0, len1, 1):
    print(tup1[i] , end="\t")

print()

for j in range(len1-1, 0-1 , -1):
    print(tup1[j], end="\t")

print()

for k in tup1:
    print(k , end="\t")