from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math


hub = MSHub()

distance_sensor = DistanceSensor('B')

# Switch on the top light of the Distance Sensor.
distance_sensor.light_up(5, 5, 0, 0)


# Measure the distance between the Distance Sensor and object in centimeters and inches.
while True:
    dist_perc = distance_sensor.get_distance_percentage(True)
    print( '%:', dist_perc)
