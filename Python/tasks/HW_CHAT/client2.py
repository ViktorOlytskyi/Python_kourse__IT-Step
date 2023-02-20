import socket
import threading

def receive_messages(sock):
    """
    Функція для прийому повідомлень від сервера
    """
    while True:
        try:
            message = sock.recv(1024).decode()
            print(message)
        except:
            break

# Підключення до сервера
HOST = 'localhost'
PORT = 8000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# Аутентифікація
authenticated = False
while not authenticated:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    s.sendall(username.encode())
    s.sendall(password.encode())
    response = s.recv(1024).decode()
    if response == "AUTHENTICATED":
        authenticated = True
    else:
        print("Invalid username or password")

# Створення нового потоку для прийому повідомлень від сервера
recv_thread = threading.Thread(target=receive_messages, args=(s,))
recv_thread.start()

# Відправка повідомлень в чат
while True:
    message = input()
    s.sendall(message.encode())
    if message.lower() == "exit":
        break

s.close()
