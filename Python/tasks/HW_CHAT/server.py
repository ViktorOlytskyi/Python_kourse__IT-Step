import socket
import threading

def broadcast_message(sender_conn, message):
    """
    Функція для надсилання повідомлення всім іншим користувачам
    """
    for conn in connections:
        if conn != sender_conn:
            conn.sendall(message.encode())


def handle_client(conn):
    """
    Функція для обробки запитів від клієнта
    """
    authenticated = False
    while not authenticated:
        username = conn.recv(1024).decode()
        password = conn.recv(1024).decode()
        with open("users.txt", "r") as f:
            for line in f:
                user, pwd = line.strip().split(":")
                if user == username and pwd == password:
                    authenticated = True
                    break
        if authenticated:
            conn.sendall("AUTHENTICATED".encode())
        else:
            conn.sendall("UNAUTHORIZED".encode())

    print(f"New user connected: {username}")

    # Додамо нового користувача до списку з'єднань
    connections.append(conn)
    usernames.append(username)

    # Надсилаємо повідомлення про нового користувача всім іншим користувачам
    message = f"{username} joined the chat"
    broadcast_message(conn, message)

    while True:
        try:
            data = conn.recv(1024).decode()
            if data.lower() == "exit":
                conn.sendall("exit".encode())
                conn.close()
                print(f"User {username} disconnected")
                connections.remove(conn)
                usernames.remove(username)
                message = f"{username} left the chat"
                broadcast_message(conn, message)
                break
            else:
                message = f"{username}: {data}"
                broadcast_message(conn, message)
        except:
            conn.close()
            print(f"User {username} disconnected")
            connections.remove(conn)
            usernames.remove(username)
            message = f"{username} left the chat"
            broadcast_message(conn, message)
            break



# Створення серверного сокету
HOST = 'localhost'
PORT = 8000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()

print(f"Server started on {HOST}:{PORT}")

# Списки для зберігання з'єднань та імен користувачів
connections = []
usernames = []

while True:
    conn, addr = s.accept()
    # Створення нового потоку для обробки запиту клієнта
    client_thread = threading.Thread(target=handle_client, args=(conn,))
    client_thread.start()
