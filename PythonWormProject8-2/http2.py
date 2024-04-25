import requests

r = requests.get("http://192.168.0.64:80/Helloproject8/public_html/index.html")

print(r.status_code)