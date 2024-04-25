from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("https://zh.wikipedia.org/zh-tw/%E8%BF%AA%E4%B8%BD%E7%83%AD%E5%B7%B4%C2%B7%E8%BF%AA%E5%8A%9B%E6%9C%A8%E6%8B%89%E6%8F%90").read().decode("utf-8")

soup = BeautifulSoup(html, "html.parser")

kdata = soup.find(class_= "wikitable")
tdata = kdata.find_all("td")

len1= len(tdata)

for i in range(1, len1+1):
    if i%4==0:
        print((tdata[i - 1].text).strip(),end="\n")
        print("---------------------")
    else:
        print((tdata[i - 1].text).strip(),end="\t")




#for i in range(0, 5, 1):
    #print(kdata[i].text.strip())
