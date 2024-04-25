a = [12 ,56, 99, 21, 52]

len1 = len(a)

for j in range(len1-1, 0-1, -1):
    print("index",j,"==>",a[j])# end="\t" )


print()

i= len1 -1
for _ in a:
    print(a[i],end="\t")
    i -=1

