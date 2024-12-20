import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 5001))
server_socket.listen(1)
print(f"Server is listening on {'127.0.0.1'}:{5001}")

# Accept a connection from the client
client_socket, client_address = server_socket.accept()
print(f"Connection from {client_address} has been established.")

# Receive the file data from the client
with open("received_file.txt", "wb") as file:
    while True:
        data = client_socket.recv(1024)  # Receive data in chunks
        if not data:
            break  # Break if no more data is sent
        file.write(data)

print("File received and saved as 'received_file.txt'.")

# Close connections
client_socket.close()
server_socket.close()

# updated code 
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

