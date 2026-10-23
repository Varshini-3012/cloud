import socket
import pickle


class DataObject:
    def __init__(self, name, values):
        self.name = name
        self.values = values


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 12346))

obj = DataObject("SampleData", [10, 20, 30, 40])
data = pickle.dumps(obj)

client.sendall(data)

response = client.recv(1024).decode()
print("Server response:", response)

client.close()