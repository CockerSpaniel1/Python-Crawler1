mylist1 = []

mylist1.append("java")
mylist1.append("javascript")
mylist1.append("delphi")
mylist1.append("c++")
mylist1.append("jquery")
mylist1.insert(2, "php")

for i in mylist1:
    print(i , end="\t")
print()

for j in range(0 , len(mylist1), 1):
    print(mylist1[j], end="\t")

print()


