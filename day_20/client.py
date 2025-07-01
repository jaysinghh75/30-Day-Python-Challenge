import socket

# Step 1: Create socket and connect to server
client_socket = socket.socket()
client_socket.connect(("localhost", 9090))

# Step 2: Define the URL to be sent
python_official_url = "https://www.python.org"

# Step 3: Send the URL to the server
client_socket.send(python_official_url.encode('utf-8'))
print(f"URL sent to the server: {python_official_url}")

# Step 4: Close the connection
client_socket.close()
print("Client connection closed.")
