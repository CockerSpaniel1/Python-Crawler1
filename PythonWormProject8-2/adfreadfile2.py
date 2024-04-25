with open("jungdb2.txt" , "r") as f:
    data = f.readlines()
    print("%s" % data)

len1=len(data)
print(len1)
print(data[0])
print(data[2])

f.close()