from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("https://briian.com/2006/").read().decode("utf-8")

soup = BeautifulSoup(html, "html.parser")
kdata = soup.find_all("p")
len1 =len(kdata)

for i in range(0, len1):
    print(kdata[i].text)
