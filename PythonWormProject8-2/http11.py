import requests

r = requests.get("http://192.168.0.64:80/Helloproject8/public_html/chingjung1.txt")
r.encoding = "utf-8"

if r.status_code == requests.codes.ok:
    print(r.text)