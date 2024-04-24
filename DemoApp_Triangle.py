#!/usr/bin/env python
import time
import argparse
from flyt_python import api

# Instantiate the Flyt drone navigation class
drone = api.navigation(timeout=120000)

# Sleep for at least 3 seconds for the drone interface to initialize properly
time.sleep(3)

# Parse command line arguments
parser = argparse.ArgumentParser(description='Process a float value.')
parser.add_argument('side', metavar='side_length', type=float, help='side length of the square')
args = parser.parse_args()

# Let's fly!
side_length = args.side

print("Preparing for takeoff...")
drone.take_off(10.0)

print('Flying in a square with side length', side_length)
setpoints = [(side_length, 0, 0), (0, side_length, 0), (-side_length, 0, 0), (0, -side_length, 0)]
for setpoint in setpoints:
    drone.position_set(*setpoint, relative=True)

print("Initiating landing...")
drone.land(False)
print('Mission completed!')

# Shutdown the drone instance
drone.disconnect()
