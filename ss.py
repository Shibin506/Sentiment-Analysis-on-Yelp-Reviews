import socket

HOST = 'localhost'
PORT = 8899
message = "The food was great and ambiance was perfect.\n"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(message.encode('utf-8'))

print("✅ Sent review to NiFi")
