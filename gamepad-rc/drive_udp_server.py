import socket
import time
from gpiozero import CamJamKitRobot  # Import the CamJam GPIO Zero Library

robot = CamJamKitRobot()

# Set the relative speeds of the two motors, between 0.0 and 1.0
leftmotorspeed = 0.5
rightmotorspeed = 0.5

motorforward = (leftmotorspeed, rightmotorspeed)
motorbackward = (-leftmotorspeed, -rightmotorspeed)
motorleft = (leftmotorspeed, 0)
motorright = (0, rightmotorspeed)

def forward(duration: float) -> None:
    """Move the robot forward for a specified duration."""
    robot.value = motorforward
    time.sleep(duration)
    robot.stop()

def backward(duration: float) -> None:
    """Move the robot backward for a specified duration."""
    robot.value = motorbackward
    time.sleep(duration)
    robot.stop()

def left(duration: float) -> None:
    """Turn the robot left for a specified duration."""
    robot.value = motorleft
    time.sleep(duration)
    robot.stop()

def right(duration: float) -> None:
    """Turn the robot right for a specified duration."""
    robot.value = motorright
    time.sleep(duration)
    robot.stop()

def udp_server(host='0.0.0.0', port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    
    # Set socket to non-blocking mode
    server_socket.settimeout(0.25)  # seconds
    
    print(f"UDP Server listening on {host}:{port}")
    print("Press Ctrl+C to stop the server")
    
    try:
        while True:
            try:
                # Try to receive data
                data, client_address = server_socket.recvfrom(1024)
                move = data.decode('utf-8')
                duration = 0.25 # seconds
                if move in globals() and callable(globals()[move]):
                    globals()[move](duration)
                    print(f"Executed {move} for {duration} seconds")
                else:
                    print(f"Error: '{move}' is not a valid movement. Available: forward, backward, left, right")
                    print(f"DEBUG|Received from {client_address}: {move}")
            except socket.timeout:
                # No data received within timeout period
                time.sleep(0.25)
                
    except KeyboardInterrupt:
        print("\nServer stopped by user")
    finally:
        server_socket.close()

if __name__ == "__main__":
    udp_server()