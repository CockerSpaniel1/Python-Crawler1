from urllib.request import urlopen
from bs4 import BeautifulSoup

html =urlopen("https://ingtt.com/10840/html-table").read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

kdata =soup.find_all(id="tds")

len1 = len(kdata)

for j in range(0,3):
    udata = kdata[j].find_all("td")
    len2 = len(udata)

    for i in range(1, len2+1):
        print(i, end="\t")

        if (i%3==0):
            print("#", end="")
            print((udata[i-1].text).strip(), end="\n")

        else:
            print("@", end="")
            print((udata[i-1].text).strip(), end="\t")

    print("------------------------------------------")






