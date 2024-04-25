a = [12 ,56, 99, 21, 52]

len1 = len(a)

for j in range(0, len1, 1):
    print(a[j])

for j in range(0, len1, 1):
    print(a[j], end="\t")

#偶數索引值----------------
for j in range(0, len1, 1):
    if j%2==0:
        print(a[j] , end="\t")

print()
#奇數索引值----------------
for j in range(0, len1, 1):
    if j%2!=0:
        print(a[j] , end="\t")

print()
#偶數值----------------
for j in range(0, len1, 1):
    if a[j]%2==0:
        print(a[j] , end="\t")

print()
#奇數值----------------
for j in range(0, len1, 1):
    if a[j]%2!=0:
        print(a[j] , end="\t")



for h in a:
    print(h, end='\t')

print()

k = 1
for p in a:
    print("%d==>%d" % (k,p))
    k+=1




