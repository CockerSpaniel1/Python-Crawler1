from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.bsnet.com.tw/").read().decode("utf-8")

soup = BeautifulSoup(html, "html.parser")

print(soup.title.text)