import requests

r = requests.get("http://192.168.0.64:80/Helloproject8/public_html/chingjung3.txt")
r.encoding = "utf-8"

if r.status_code == requests.codes.ok:

    dat = r.text
    print(dat)

    list2 = dat.split('\r\n')
    len1 = len(list2)

    print("list2", list2)

    for i in range(0 , len1, 1):
        kdat = list2[i]
        list3 = kdat.split(',')
        len2 = len(list3)

        print("kdat",kdat)
        print("list3",list3)

        for j in range(0, len2, 1):
            print(list3[j])
        print()