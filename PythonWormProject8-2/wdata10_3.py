from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("https://tw.pixtastock.com/tags/%E5%90%88%E6%AD%A1%E5%B1%B1").read().decode("utf-8")

soup = BeautifulSoup(html, "html.parser")
kdata = soup.find(class_="global-header-nav-pc__pulldown")

tdata = kdata.find_all("li")
len1 =len(tdata)

for i in range(0, len1, 1):
    print(tdata[i].text.strip())
