import requests

r = requests.get("http://192.168.0.64:80/Helloproject8/public_html/index.html")

if r.status_code == requests.codes.ok:
    print("網路通訊正常")