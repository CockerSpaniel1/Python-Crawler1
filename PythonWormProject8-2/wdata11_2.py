from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("http://192.168.0.64/Helloproject8/public_html/wchin3.html").read().decode("utf-8")

soup = BeautifulSoup(html ,"html.parser")
#kdata = soup.find_all("tr")
kdata = soup.find_all("td")

len1 = len(kdata)

#for i in range(0, len1):
#    kdata2 = kdata[i].find_all("td")
#    len2 = len(kdata2)
#
#    for j in range(0, len2):
#        print(kdata2[j].text, end="\t\t")
#     print()

for i in range(1, len1+1):
    #i = [0,1,2,3,4] =>i =range(1,5+1)=[1,2,3,4,(5)]
    if(i%5==0):
        #if start=0 => 0%5==True => X =>>start = 1
        print((kdata[i - 1].text).strip(), end="\n")
        print("----------------------------------")

    else:
        print((kdata[i -1].text).strip(), end="\t")
