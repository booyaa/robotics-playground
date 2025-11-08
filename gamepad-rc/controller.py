from hid_gamepad import hid_gamepad
from hid_gamepad import list_gamepads
import time
import os
import argparse
import socket

parser = argparse.ArgumentParser()
parser.add_argument("--host", required=True, help="UDP server hostname")
parser.add_argument("--port", type=int, default=12345, help="UDP server port")
args = parser.parse_args()

available_gamepads = list_gamepads()

def udp_client(host, port, message):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    try:
        client_socket.sendto(message.encode('utf-8'), (host, port))
        print(f"Sent message to {host}:{port}: {message}")
        
    except Exception as e:
        print(f"Error sending message: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    if available_gamepads:
        selected_gamepad = 0 # should be USB gamepad
        my_gamepad = hid_gamepad() 
        if my_gamepad.connect(available_gamepads[selected_gamepad]):
            print("\nConnection established with selected gampad.")
            print("Reporting gampad raw input states.")
            while True:
                if my_gamepad.update_state():
                    time.sleep(100/1000)
                    report = my_gamepad.raw_inputs
                    
                    if report[0] == 0:
                        udp_client(args.host, args.port, "left")
                    elif report[0] == 255:
                        udp_client(args.host, args.port, "right")
                    elif report[1] == 0:
                        udp_client(args.host, args.port, "forward")
                    elif report[1] == 255:
                        udp_client(args.host, args.port, "backward")
                    elif report[0] == 127 and report[1] == 127:
                        pass # neutral position, do nothing
                else:
                    if my_gamepad.is_connected is False:
                        my_gamepad.reconnect()
                        time.sleep(2000/1000)
    else:
        print("\nUnable to find gamped devices.")