import http.client
conn = http.client.HTTPSConnection("beda.pnzgu.ru")
# отправляем запрос на сервер методом GET
conn.request("GET", "/anatoly/")
r1 = conn.getresponse()
print(r1.read().decode())

