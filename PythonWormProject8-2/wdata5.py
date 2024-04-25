from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("http://192.168.0.64/Helloproject8/public_html/chin3.html").read().decode("utf-8")

soup = BeautifulSoup(html, "html.parser")
print(soup.font.text)