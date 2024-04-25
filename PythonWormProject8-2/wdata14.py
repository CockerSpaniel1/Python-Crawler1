from bs4 import BeautifulSoup
from urllib.request import urlopen
import lxml

html = urlopen("http://192.168.0.64/Helloproject8/public_html/wchin4.html").read().decode("utf-8")

soup = BeautifulSoup(html, "lxml")
kdata = soup.find(id="a2")
print(kdata.string)