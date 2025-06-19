import socket
import time

HOST = 'localhost'
PORT = 9999

# Create a socket
s = socket.socket()
s.bind((HOST, PORT))
s.listen(1)

print("✅ Server is waiting for connection...")
conn, addr = s.accept()
print(f"🔌 Connected to client: {addr}")

# Read reviews from file and send line by line
with open('yelp_reviews.txt', 'r') as file:
    for line in file:
        review = line.strip()
        print(f"📤 Sending review: {review}")
        conn.send((review + '\n').encode('utf-8'))
        time.sleep(2)

print("✅ All reviews sent. Closing connection.")
conn.close()
