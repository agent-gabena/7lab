import socket
students = {"Авдонин" : "Антон", "Яблоновский" : "Илья",}
with socket.create_server(('',7777)) as serversocket:
    while True:
        client_socket, address = serversocket.accept()
        print('Адрес клиента:', address)
        greeting = "Введите свою фамилию\n".encode()
        client_socket.send(greeting)
        data = client_socket.recv(4096)
        if students.setdefault(data.decode()[:-1]) == None:
            err = "Ошибка, такой студент в группе не учится\n".encode()
            client_socket.send(err)
            client_socket.close()
        else:
            print(students.setdefault(data.decode()[:-1]))
            answer = str("Привет, "+students.setdefault(data.decode()[:-1])+"\n").encode()
            client_socket.send(answer)
            print('Клиент прислал:', data.decode())
            client_socket.close()