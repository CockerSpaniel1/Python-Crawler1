from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://192.168.0.64:80/Helloproject8/public_html/chin2.html").read().decode("utf-8")

soup = BeautifulSoup(html, "html.parser")

print(soup.title.text)