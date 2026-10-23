
import socket

client = socket.socket()
client.connect(("localhost", 5000))

marks = input("Enter marks separated by commas: ")
client.send(marks.encode())

print("\nServer Response:")
print(client.recv(1024).decode())

client.close()
