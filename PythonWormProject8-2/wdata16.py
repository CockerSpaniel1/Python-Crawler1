from bs4 import BeautifulSoup
from urllib.request import urlopen
import lxml

html = urlopen("http://192.168.0.64/Helloproject8/public_html/wchin5.html").read().decode("utf-8")

soup =BeautifulSoup(html, "lxml")
#kdata = soup.find(class_="c1")
kdata = soup.find_all(attrs={"data-c":"c1"})

for t in kdata:
    print(t.string)