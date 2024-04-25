import requests

xid = input("輸入取值變號")

r = requests.get("http://192.168.0.64:80/Helloproject8/public_html/pythonchin3.php",params={"key1":xid})

if r.status_code == requests.codes.ok:
    data = r.text
    print(data)
    print()
    data2 = data.split("-")
    for x in data2:
        print(x)
