
import socket
import threading

def handle_client(conn, addr):
    print("Connected:", addr)
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            message = data.decode()
            print(f"{addr}: {message}")
            conn.sendall(("Server received: " + message).encode())
        except OSError:
            break
    conn.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(("localhost", 12345))
server.listen()

print("Message server is running...")

while True:
    conn, addr = server.accept()
    threading.Thread(
        target=handle_client, args=(conn, addr), daemon=True
    ).start()
