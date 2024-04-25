data = ["java","c++","delphi", "c++", "jquery", "c++"]

qp = "c++"
#mylist = []
str1 = ""

len1 = len(data)
for i in range(0, len1, 1):

    t = data[i]

    if (qp == t):
        #mylist.append(i)
        str1 += str(i)+" "

print("%s在串列中的第[ %s]元素" % (qp, str1) )

