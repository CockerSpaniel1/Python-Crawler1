from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("https://tw.pixtastock.com/tags/%E5%90%88%E6%AD%A1%E5%B1%B1").read().decode("utf-8")

soup = BeautifulSoup(html, "html.parser")

kdata = soup.find_all(class_="global-header-nav-pc__pulldown")
len1 =len(kdata)
#print("kdata",kdata)

for i in range(0,len1 ):
    print(i)
    tdata = kdata[i].find_all("li")
    #print("tdata",tdata)
    len2 =len(tdata)

    for j in range(0, len2, 1):
        print(j, tdata[j].text.strip())

    print("---------------------------------")
