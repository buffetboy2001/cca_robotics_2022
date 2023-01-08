from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math

hub = MSHub()

motor_pair = MotorPair('E', 'A')

#move 4 cm in one direction(steering = 0) at half speed
motor_pair.move(4, 'cm', 0, 50)
#move 2 rotations in opposite directions (steering = 100) at default speed
motor_pair.move(2, 'rotations', steering=100)
#move for 3 seconds on opposite directions the other way at maximum speed (100)
motor_pair.move(3, 'seconds', steering=-100, speed = 100)