
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 12345))

print("Connected to server. Type 'exit' to quit.")

while True:
    message = input("Enter message: ")
    if message.lower() == "exit":
        break

    client.sendall(message.encode())
    response = client.recv(1024).decode()
    print(response)

client.close()
