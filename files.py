import socket

def Server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost",5000))
    server.listen(1)

    print("Sever is listening...")

    client, add = server.accept()

    print(f"Connection established at {add}")

    data = client.recv(1024).decode('utf-8')

    with open("Received.txt", "w") as server_file:
        server_file.write(data)

    client.sendall("File saved".encode('utf-8'))

Server()
