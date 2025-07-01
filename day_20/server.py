import socket
import requests

# Step 1: Create the socket object
server_socket = socket.socket()

# Step 2: Allow the server to reuse the port even if it's in TIME_WAIT state
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Step 3: Bind the server to localhost on port 9090
server_socket.bind(("localhost", 9090))

# Step 4: Start listening for incoming connections
server_socket.listen(1)

print("Server is running and waiting for a client connection...\n")

try:
    # Step 5: Accept a connection from a client
    client_conn, client_addr = server_socket.accept()
    print(f"Connected with client at {client_addr}")

    # Step 6: Receive URL data sent by the client
    received_url = client_conn.recv(1024).decode('utf-8')
    print(f"URL received from client: {received_url}")

    # Step 7: Fetch the contents of the given URL
    try:
        response = requests.get(received_url)
        print("\nWebpage content (first 1000 characters):\n")
        print(response.text[:1000])
    except Exception as e:
        print("Error fetching the webpage:", e)

    # Step 8: Close the connection with the client
    client_conn.close()
    print("Connection with client closed.")

except KeyboardInterrupt:
    print("\nServer manually stopped.")

finally:
    # Step 9: Always close the server socket
    server_socket.close()
    print("Server socket closed.")
