from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math


# Create your objects here.
hub = MSHub()


# Write your program here.
hub.speaker.beep()


motor_a = Motor('A')

# Run the motor to position 175 degrees.
motor_a.run_to_position(175, 'clockwise', 75)
# Run the motor to position 0 degrees, aligning the markers.
motor_a.run_to_position(0)