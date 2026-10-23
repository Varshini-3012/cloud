import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12345))
server.listen(1)

print("Server is waiting for a connection...")
conn, addr = server.accept()
print("Connected to:", addr)

data = conn.recv(1024).decode()
print("Received:", data)

numbers = list(map(int, data.split()))
total = sum(numbers)

conn.send(str(total).encode())
print("Sum sent to client:", total)

conn.close()
server.close()