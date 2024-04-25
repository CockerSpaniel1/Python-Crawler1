from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("http://192.168.0.64/Helloproject8/public_html/wchin3.html").read().decode("utf-8")

soup = BeautifulSoup(html ,"html.parser")
kdata = soup.find_all("td")

len1 = len(kdata)
tdata = []
udata = []

for i in range(1, len1+1):
    if(i%5==0):
        udata.append((kdata[i-1].text).strip())
        tdata.append(udata)
        udata = []
    else:
        udata.append((kdata[i-1].text).strip())



while True:
    ch = int(input("請選擇(1)編號查詢(2)完全結束: "))
    if ch ==2:
        quit()

    if ch ==1:
        sid = input("請輸入查詢編號: ")
        len1= len(tdata)

        for k in range(1, len1):
            tid = tdata[k][0]

            if tid == sid:
                for q in tdata[k]:
                    print(q, end="\t")
                print()


