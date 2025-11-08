# Gamepad Remote Controller

## Gamepad used

I used [SNES style USB](https://thepihut.com/products/raspberry-pi-compatible-usb-gamepad-controller-snes-style) gamepad.

## Code

### Attributions

I patched [hid_gamepad.py](./hid_gamepad.py) [ppieczywek/hid_gamepad](https://github.com/ppieczywek/hid_gamepad/tree/main) to scan for Gamepads.

controller.py is based off [generic_example.py](https://github.com/ppieczywek/hid_gamepad/blob/main/generic_example.py) from the abovementioned repo.

## Usage

The assumption is that both computers are on the same local network.

### On the pi connected to the robotic kit

- Run `drive_udp_server.py` on the pi with the robot kit.

### On the computer with the gamepad

```sh
uv venv
uv pip install hidapi
python controller.py
```