#!/usr/bin/env pybricks-micropython


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

left_motor = Motor(Port.B)
right_motor = Motor(Port.A)

right_sensor = ColorSensor(Port.S1)
left_sensor = ColorSensor(Port.S2)
# Write your program here.  
ev3.speaker.beep()
worth = left_sensor.reflection()
print(worth)

robot = DriveBase(left_motor, right_motor, wheel_diameter=65.5, axle_track=104)

# Go forward and backwards for one meter.
#robot.straight(1000)
ev3.speaker.beep()

#robot.straight(-1000)
ev3.speaker.beep()

# Turn clockwise by 360 degrees and back again.
#robot.turn(360)
ev3.speaker.beep()

#robot.turn(-360)
ev3.speaker.beep()  

#fubjar detta 123
#vill testa att det alltid funkar please
#dasdasdaad

#uggabogga
#dasdasdaad
#hejsan
#heeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeej
#adosufyhbpoiasdjbngfpiadjfg
#adosufyhbpoiasdjbngfpiadjfg
#ich bin ein junge
#skinflöjt ja
#dededededee
#vafan
