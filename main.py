#!/usr/bin/env pybricks-micropython


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

#Motorer
left_motor = Motor(Port.B)
right_motor = Motor(Port.A)

#Färgsensorer
right_sensor = ColorSensor(Port.S1)
left_sensor = ColorSensor(Port.S2)

#Gör så att båda motorerna kan gå samtidigt
robot = DriveBase(left_motor, right_motor, wheel_diameter=65.5, axle_track=104)

#Värden på färgena
Black = 10
Both_White = 50

#Värde på hastigheten på roboten(antar mm/s)
Drive_Speed = 100

#Oändlig loop
while True:
    #1. Failsafe
    #2. Höger Sensor ser svart svänger höger
    #3. Vänster Sensor ser svart svänger vänster
    #4. Allt är fine kör rakt

    rsensor = right_sensor.reflection()
    lsensor = left_sensor.reflection()
    both_sensor = rsensor + lsensor
    
    if both_sensor > Both_White:
        turn_rate = 35
    elif rsensor < Black:
        turn_rate = 20
    elif lsensor < Black:
        turn_rate = -20
    else:
        turn_rate = 0
    
    robot.drive(Drive_Speed, turn_rate)
    