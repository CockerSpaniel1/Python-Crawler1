import requests

r = requests.get("http://192.168.0.64:80/Helloproject8/public_html/pythonchin2.php",params={"key1":"p1002"})

if r.status_code == requests.codes.ok:
    print(r.text)
