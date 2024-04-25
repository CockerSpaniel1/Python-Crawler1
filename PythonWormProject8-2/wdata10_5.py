from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("https://tw.pixtastock.com/tags/%E5%90%88%E6%AD%A1%E5%B1%B1").read().decode("utf-8")

soup = BeautifulSoup(html, "html.parser")

kdata = soup.find_all(class_="item-list--large__wrap")
len1 =len(kdata)
print(len1)

p=1
for i in range(0, len1):
    tdata = kdata[i].find("p")
    print(p,"=======>", tdata.text)

    p += 1