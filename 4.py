import http.client
conn = http.client.HTTPSConnection("beda.pnzgu.ru")
# отправляем запрос на сервер методом GET
conn.request("GET", "/anatoly/anatoly.webp")
r = conn.getresponse()
with open('myfile', 'wb') as f:
    f.write(r.read())
