from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("http://192.168.0.64/Helloproject8/public_html/wchin1.html").read().decode("utf")


soup = BeautifulSoup(html, "html.parser")
kdata = soup.find_all('p')
print(kdata)