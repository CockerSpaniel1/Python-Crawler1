import requests

r = requests.get("http://192.168.0.64:80/Helloproject8/public_html/chingjung2.csv")
r.encoding = "utf-8"

if r.status_code == requests.codes.ok:
    dat = r.text
    print(dat)
    print()
    list1 = dat.split(',')
    len1 = len(list1)
    j = 1
    for i in range(0, len1, 1):
        print(j , "=>", list1[i])
        j += 1