"""
Prompt

In this assignment, you will develop a simple Web server in Python that is capable of processing only one request.

Specifically, your Web server will

(i) create a connection socket when contacted by a client (browser);

(ii) receive the HTTP request from this connection;

(iii) parse the request to determine the specific file being requested;

(iv) get the requested file from the server’s file system;

(v) create an HTTP response message consisting of the requested file preceded by header lines; and

(vi) send the response over the TCP connection to the requesting browser. If a

browser requests a file that is not present in your server, your server should return a

“404 Not Found” error message.


Implementation Guide:
1. Socket Creation and Binding: The server listens for connections on localhost and port 8080.
2. Accepting Connections: When a client (like a browser) connects, the server accepts it.
3. Receiving Request: The server reads the HTTP request from the client.
4. Parsing Request: The server extracts the filename from the request.
5. Serving the File: If the file exists, it sends the file content with a 200 OK status. If not, it sends
   a 404 Not Found response.
6. Closing the Connection: Finally, the server closes the connection to the client.

This server handles only one request. For a server that handles multiple requests, you'd need to run the
connection handling code in a loop or use threading.
"""

import socket
import os

def start_server():
    # Define the IP and port to listen on
    server_ip = 'localhost'  # or use '127.0.0.1'
    server_port = 8082

    # Create a socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the IP and port
    server_socket.bind((server_ip, server_port))

    # Listen for incoming connections
    server_socket.listen(1)

    print(f"Server is ready to receive on port {server_port}...")

    while True:
        # Accept a connection from a client
        connection_socket, client_address = server_socket.accept()
        print(f"Connection established with {client_address}")

        # Receive the request message from the client
        request_message = connection_socket.recv(1024).decode()
        print(f"Received request:\n{request_message}")

        # Parse the request to get the filename
        request_lines = request_message.splitlines()
        filename = request_lines[0].split()[1]  # Extract the file path

        # Remove the leading slash '/' from the filename
        if filename == '/':
            filename = '/index.html'  # Default to index.html if no specific file is requested
        filename = filename[1:]  # Remove leading '/'

        # Check if the file exists
        if os.path.exists(filename):
            # Open and read the file
            with open(filename, 'rb') as file:
                response_body = file.read()

            # Create an HTTP response header
            response_header = 'HTTP/1.1 200 OK\r\n'
            response_header += f'Content-Length: {len(response_body)}\r\n'
            response_header += 'Content-Type: text/html\r\n'  # Adjust MIME type as needed
            response_header += '\r\n'

            # Send the response header and body to the client
            connection_socket.sendall(response_header.encode() + response_body)
        else:
            # File not found, send a 404 response
            response_header = 'HTTP/1.1 404 Not Found\r\n'
            response_body = b'<html><body><h1>404 Not Found</h1></body></html>'
            response_header += f'Content-Length: {len(response_body)}\r\n'
            response_header += 'Content-Type: text/html\r\n'
            response_header += '\r\n'

            # Send the response header and body to the client
            connection_socket.sendall(response_header.encode() + response_body)

        # Close the connection socket
        connection_socket.close()

        # Ask the user if they want to start the server again
        restart = input("Do you want to start the server again? (y/n): ").strip().lower()
        if restart != 'y':
            print("Shutting down the server...")
            break

    # Close the server socket
    server_socket.close()

# Run the server
start_server()
