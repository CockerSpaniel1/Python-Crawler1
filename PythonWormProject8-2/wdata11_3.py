from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("http://192.168.0.64/Helloproject8/public_html/wchin3.html").read().decode("utf-8")

soup = BeautifulSoup(html ,"html.parser")
kdata = soup.find_all("td")

len1 = len(kdata)
tdata = []
udata = []

for i in range(1, len1+1):
    #i = [0,1,2,3,4] =>i =range(1,5+1)=[1,2,3,4,(5)]
    if(i%5==0):
        udata.append((kdata[i-1].text).strip())
        tdata.append(udata)
        print(i ,"%5 == 0")

        print("udata= ", udata)
        udata = []
        print("append to tdata= ", tdata)
        print("reset udata= ", udata)

        print("----------------------------------")

    else:
        print(i ,"%5 != 0")
        udata.append((kdata[i-1].text).strip())
        print("udata= ", udata)
print("final")
print(tdata)


for k in tdata:
    if k[0]=="p1001":
        print(k)
