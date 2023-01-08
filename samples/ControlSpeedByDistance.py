from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math
import time


# Initialize the Distance Sensor.
wall_detector = DistanceSensor('B')
motor = Motor('A')

# Measure the distance between the Distance Sensor and object in centimeters and inches.
while (True):
    time.sleep(.1) # wait each time for 100 miliseconds before reading distance

    dist_perc = wall_detector.get_distance_percentage(True) # activate short distance
    if dist_perc == None :
        motor.stop()
    else :
        motor.start(dist_perc)


    print('percentage: ', dist_perc)