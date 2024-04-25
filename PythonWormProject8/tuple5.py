tup1 =["java", "javascript", "c++", "delphi", "php"]
mylist2 = list(tup1)
mylist2.append("jsp")
tup1 = tuple(mylist2)

len1 = len(tup1)
for i in range(0, len1):
    print(tup1[i])