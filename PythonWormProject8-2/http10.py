import requests

r = requests.post("http://192.168.0.64:80/Helloproject8/public_html/pythonchin4.php",data={"name":"chingjung"})

if r.status_code == requests.codes.ok:
    print(r.headers['Content-Type'])
    print(r.headers['Content-Length'])
    print(r.headers['Date'])
    print(r.headers['Server'])
