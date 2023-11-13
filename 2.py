import socket
import socket
students = {"Авдонин" : "Антон", "Яблоновский" : "Илья",}
with socket.socket(type=socket.SOCK_DGRAM) as serversocket:
    serversocket.bind(('',5555))
    d, a = serversocket.recvfrom(4096)
    greeting = "Введите свою фамилию\n".encode()
    while True:
        serversocket.sendto(greeting, a)
        data, address = serversocket.recvfrom(4096)
        print('Адрес клиента:', address)
        if students.setdefault(data.decode()[:-1]) == None:
            err = "Ошибка, такой студент в группе не учится\n".encode()
            serversocket.sendto(err, address)
        else:
            print(students.setdefault(data.decode()[:-1]))
            answer = str("Привет, "+students.setdefault(data.decode()[:-1])+"\n").encode()
            serversocket.sendto(answer, address)
            print('Клиент прислал:', data.decode())
