import socket
import time

HOST = 'localhost'  # or use your IP address if sending from another machine
PORT = 9999         # This should match the port in NiFi ListenTCP

# Sample Yelp-style reviews
reviews = [
    "The food was amazing!",
    "Terrible service and rude staff.",
    "Pretty average experience overall.",
    "Excellent ambience and great value!",
    "Won't visit again. Very disappointed."
]

# Create TCP socket and send data
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    for review in reviews:
        s.sendall((review + "\n").encode())
        print(f"Sent: {review}")
        time.sleep(1)  # Small delay between messages
