mylist1 = []
mylist2 = []

mylist1.append("java")
mylist1.append("javascript")
mylist1.append("delphi")
mylist1.append("anjular")
mylist1.append("jquery")

len1 = len(mylist1)
for i in range(0, len1, 1):

    kv = mylist1[i]
    len2 = len(kv)

    for j in range(0 , len2, 1):

        tv = kv[j]

        if (tv == "v") or (tv == "u"):

            mylist2.append(kv)



for i in mylist2:
    print(i)



#get mylist1 length
#loop through 0 ~ length1 with i
    #use i get word kv
    #get word length

    #loop through 0 ~length2 with j
    #use j get charater tv
    # compare tv with u , v
        # append to mylist2




















