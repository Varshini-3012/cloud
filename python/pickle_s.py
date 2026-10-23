import socket
import pickle


class DataObject:
    def __init__(self, name, values):
        self.name = name
        self.values = values


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12346))
server.listen(1)

print("Server is waiting for a connection...")
conn, addr = server.accept()

data = conn.recv(4096)
obj = pickle.loads(data)

print("Object received:", obj.name)
total = sum(obj.values)

response = f"Sum of values: {total}"
conn.send(response.encode())

print(response)

conn.close()
server.close()