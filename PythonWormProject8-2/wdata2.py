from urllib.request import urlopen

html = urlopen("http://192.168.0.64:80/Helloproject8/public_html/chin2.html").read().decode("utf-8")

print(html)