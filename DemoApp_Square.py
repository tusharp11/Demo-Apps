#!/usr/bin/env python
import time
from flyt_python import api

# Instantiate the Flyt drone navigation class
drone = api.navigation(timeout=120000)

# Wait for the drone interface to initialize properly (at least 3 seconds)
time.sleep(3)

# Perform takeoff
print('Executing takeoff...')
drone.take_off(6.5)

# Move along the setpoints
print('Moving along the setpoints...')
setpoints = [(5, 0, 0), (0, 5, 0), (-5, 0, 0), (0, -5, 0)]
for setpoint in setpoints:
    drone.position_set(*setpoint, relative=True)

# Perform landing
print('Executing landing...')
drone.land(async=False)

# Disconnect the drone instance
drone.disconnect()

 