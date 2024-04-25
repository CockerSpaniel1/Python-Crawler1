tup1 = (12, 56.8 ,"范楨", True, "A")

#for i in tup1:

#    type1 = type(i)

#    if type1 == int or type1 == float:
#        print(i)

for k in tup1:
    print(k)

print()

len1 = len(tup1)
for i in range(0, len1):
    x = type(tup1[i])
    if (str(x)== "<class 'int'>" or str(x) =="<class 'float'>"):
        print(tup1[i], end='\t')
