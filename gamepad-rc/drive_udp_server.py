import socket
import time

def udp_server(host='0.0.0.0', port=12345):
    """Create and run a UDP server that listens for messages on the local network."""
    # Create UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    
    # Set socket to non-blocking mode
    server_socket.settimeout(0.25)  # 0.25 second timeout
    
    print(f"UDP Server listening on {host}:{port}")
    print("Press Ctrl+C to stop the server")
    
    try:
        while True:
            try:
                # Try to receive data
                data, client_address = server_socket.recvfrom(1024)
                message = data.decode('utf-8')
                print(f"DEBUG|Received from {client_address}: {message}")
                #TODO: waiting for integration with robot drive commands
            except socket.timeout:
                # No data received within timeout period
                time.sleep(0.25)
                
    except KeyboardInterrupt:
        print("\nServer stopped by user")
    finally:
        server_socket.close()

if __name__ == "__main__":
    udp_server()