"""A script to control the robot
A lot of the initial code was taken from https://github.com/CamJam-EduKit/EduKit3/
"""
import argparse
import time  # Import the Time library
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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Control the robot with specified duration")
    parser.add_argument("--duration", type=float, default=1.0, help="Duration for robot movements in seconds")
    parser.add_argument("--move", type=str, help="Type of movement (forward, backward, left, right)")
    args = parser.parse_args()
    duration = args.duration
    move = args.move
    
    try:
        if move:
            if move in globals() and callable(globals()[move]):
                globals()[move](duration)
                print(f"Executed {move} for {duration} seconds")
            else:
                print(f"Error: '{move}' is not a valid movement. Available: forward, backward, left, right")
        else:
            # Default behavior if no move specified
            forward(1.0)
            backward(1.0)
            left(0.5)
            right(0.5)
    except KeyboardInterrupt:
        print("Robot stopped by User")
        robot.stop()
