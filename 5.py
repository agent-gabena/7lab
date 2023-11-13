import http.client
from html.parser import HTMLParser
class MyParser(HTMLParser):
 # вызывается при парсинге любого открывающего тега
    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            for attr in attrs:
                if attr[0] == 'src':
                    print(attr[1])
parser = MyParser()
conn = http.client.HTTPSConnection("beda.pnzgu.ru")
# отправляем запрос на сервер методом GET
conn.request("GET", "/anatoly/")
r = conn.getresponse()
a = str(parser.feed(r.read().decode()))
print(a)
parser.close()
