
import socket
import os

server = socket.socket()
server.bind(("localhost", 5002))
server.listen(1)

print("Server waiting...")
conn, addr = server.accept()

filename = conn.recv(1024).decode()

try:
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()

    lines = len(content.splitlines())
    words = len(content.split())
    size = os.path.getsize(filename)

    response = (
        f"Lines: {lines}\n"
        f"Words: {words}\n"
        f"File Size: {size} bytes"
    )
except FileNotFoundError:
    response = "Error: File not found on server."

conn.sendall(response.encode())
conn.close()
server.close()
