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

#len2 = len(tdata)

#for k in range(0, len2):
#    if k==0:
#        print("各欄位名稱: ")
#        for c in tdata[k]:
#            print( c, end=" ")
#        print("\n紀錄資料: ")
#    else:
#        for c in tdata[k]:
#            print( c, end=" ")
#        print("")


lenr = len(tdata)
lenf = len(tdata[0])

print("各欄位名稱: ")
for f in range(0, lenf):
    print(tdata[0][f], end="\t")

print("紀錄資料: ")
for i in range(1, lenr):
    for j in range(0, lenf):
        print(tdata[i][j], end=" ")
    print(" ")

