from mindstorms import MSHub, ColorSensor
from mindstorms.operator import not_equal_to, equal_to
from mindstorms import MSHub, Motor


hub = MSHub()
paper_scanner = ColorSensor('E')
motor_a = Motor('A')


while True:
    color = paper_scanner.get_color()
    if equal_to(color, 'blue'):
        hub.status_light.on(color)
        motor_a.start(60)

    else :
        hub.status_light.on('red')
        motor_a.stop()
        