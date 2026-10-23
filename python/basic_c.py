import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 12345))

numbers = input("Enter numbers separated by spaces: ")
client.send(numbers.encode())

result = client.recv(1024).decode()
print("Sum received from server:", result)

client.close()