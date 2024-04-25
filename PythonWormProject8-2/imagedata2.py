from urllib.request import urlopen
from lxml import html

h=urlopen("http://192.168.0.64/Helloproject8/public_html/imagedata1.html").read().decode("utf-8")
kdata = html.fromstring(h)

len1 = kdata.xpath("count(/html/body/table[@id='tab1']/tr/td)")

for i in range(1, int(len1)+1 ,1):
    tdata = kdata.xpath("/html/body/table/tr/td["+str(i)+"]/img")[0]
    print(tdata.attrib['src'])