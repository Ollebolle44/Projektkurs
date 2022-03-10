#!/usr/bin/env pybricks-micropython


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Color
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
color_sensor = ColorSensor(Port.S3)
#Börjar med ett eftersom den skippar den första där uppplockaren kommer stå
deposit = 1
pickup = 0
turn_crossection = 3

#Gör så att båda motorerna kan gå samtidigt
robot = DriveBase(left_motor, right_motor, wheel_diameter=65.5, axle_track=104)

#Värden på färgena + sätter in färger
POSSIBLE_COLORS = [Color.RED, Color.GREEN, Color.BLUE, Color.WHITE]
Black = 10
Both_White = 50

#Värde på hastigheten på roboten(antar mm/s)
Drive_Speed = 100

#Oändlig loop
while True:
    #uppdatering av sensorernas värde samt summa av dem
    rsensor = right_sensor.reflection()
    lsensor = left_sensor.reflection()
    color = color_sensor.color()
    both_sensor = rsensor + lsensor
    
    #While loopen kommer sättas igång när alla bollar lämnats och används för att plocka upp nya
    
    #1. Den åkt förbi 4 färger och kommer lämna av en bollsort beroende på den sista färgen
    #2. Den åker förbi en av de fyra färgena och svänger till höger(behöver en grej så den vet när den ska svänga)
    #3. Den åker förbi en gul färg och kommer addera en variabel elr ngt för att veta när den ska svänga
    #4. Failsafe
    #5. Höger Sensor ser svart svänger höger
    #6. Vänster Sensor ser svart svänger vänster
    #7. Allt är fine kör rakt
    
    while pickup == 3:
        #linjeföljekod med samma en engångs höger sväng kod och sen en meetup kod med upplockaren
        #trycksensor när de är vid varanda -> vänta antal sekunder -> sätt pickup =0 och kör på gamla
        #programmet
        pickup = 0

    if color in POSSIBLE_COLORS and deposit==4:
        deposit = 0
        #kör tills trycksensor trycks åt?
        #sedan gör den ngn sekvens så den kommer rätt med gatesen
        #-> till nästa ifsats för att släppa bollar
        #if satser med 3 olika färgena som öppnar rätt gate beroende på färg
        if color == COLOR.BLUE:
            #blå öppna gate 1
        elif color == COLOR.GREEN:
            #grön öppna gate 2
        elif color == COLOR.RED:
            #röd öppna gate 3
        pickup +=1
        #här ksk vi ska ha en variabel som adderas med 1 och när den varit på alla 3
        #så åker den tillbaka till upplockaren?
    elif color in POSSIBLE_COLORS and turn_crossection == 4:
        #300 mm 90 grader 3 sekunder
        robot.drive_time(300, 90, 3000)
        deposit +=1
        turn_crossection = 0
    elif color == COLOR.YELLOW:
        turn_crossection += 1
    elif both_sensor > Both_White:
        turn_rate = 180
    elif rsensor < Black:
        turn_rate = 150
    elif lsensor < Black:
        turn_rate = -150
    else:
        turn_rate = 0
    
    robot.drive(Drive_Speed, turn_rate)
    