data = ["java","c++","delphi", "c++", "jquery", "c++"]
#result =>"java","delphi", "jquery"

qp = "c++"

#c = data.count(qp)
#for i in range(0, c ,1 ):
#    data.remove(qp)

for i in data:
    if i==qp:
        data.remove(i)


for j in data:
    print(j)
