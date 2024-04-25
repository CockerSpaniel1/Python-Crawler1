from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("http://192.168.0.64/Helloproject8/public_html/wchin2.html").read().decode("utf-8")

soup = BeautifulSoup(html, "html.parser")
kdata = soup.find_all("li")
len1 =len(kdata)

for i in range(0, len1):
    print(kdata[i].text)
