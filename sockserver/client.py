# ========================= Аспекты безопасности ==============================

# ----- Простой сокет-клиент для демонстрации работы с pickle-данными ---------

import pickle
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 9999))

message = sock.recv(1024)

print(message)

pickle.loads(message)

sock.close()
