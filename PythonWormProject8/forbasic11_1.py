a = 0
for i in range(1, 100+1 , 1):
    a += i
print(a)

b = 0
for j in range(0, 100+1, 1):
    if (j%2)==0:
        b += j
print(b)

c = 0
for k in range(1 , 99+1 , 1):
    if (k%2)!=0:
        c += k
print(c)

d = 0
for x in range(1, 100+1 , 1):
    if (x%3)==0 or (x%7)==0:
        d += x
print(d)

for y in range(1, 10+1):
    #y *= 0.5
    print("%.1f" % (y*0.5), end=" ")

print()
for f in range(1, 9+1, 1):
    for g in range(1 , 9+1, 1):
        h = f * g
        print("{0}x{1}={2}".format(f,g,h), end=",")
    print("\n")
