
import socket

client = socket.socket()
client.connect(("localhost", 5002))

filename = input("Enter filename: ")
client.send(filename.encode())

print("\nFile Statistics:")
print(client.recv(4096).decode())

client.close()
