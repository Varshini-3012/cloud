
import socket

server = socket.socket()
server.bind(("localhost", 5000))
server.listen(1)

print("Server waiting for client...")
conn, addr = server.accept()

data = conn.recv(1024).decode()
marks = list(map(int, data.split(",")))

total = sum(marks)
average = total / len(marks)
result = "PASS" if all(m >= 35 for m in marks) else "FAIL"

# Demonstration rank based on total marks
rank = 1 if result == "PASS" else "Not Ranked"

response = (
    f"Total: {total}\n"
    f"Average: {average:.2f}\n"
    f"Result: {result}\n"
    f"Rank: {rank}"
)

conn.send(response.encode())
conn.close()
server.close()
