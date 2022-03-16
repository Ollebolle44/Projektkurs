#!/usr/bin/env pybricks-micropython


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, TouchSensor
from pybricks.parameters import Port, Color
from pybricks.robotics import DriveBase
from pybricks.tools import wait
# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

#Motorer
left_motor = Motor(Port.B)
right_motor = Motor(Port.A)
gate_small_medium = Motor(Port.C)
gate_big = Motor(Port.D)

#Färgsensorer
right_sensor = ColorSensor(Port.S2)
left_sensor = ColorSensor(Port.S3)
color_sensor = ColorSensor(Port.S1)
#touch_sensor = 4
#Börjar med ett eftersom den skippar den första där uppplockaren kommer stå
deposit = 1
pickup = 0
turn_crossection = 3

#Gör så att båda motorerna kan gå samtidigt
robot = DriveBase(left_motor, right_motor, wheel_diameter=75.5, axle_track=104)

#Värden på färgena + sätter in färger
POSSIBLE_COLORS = [Color.RED, Color.GREEN, Color.BLUE, Color.WHITE]
Black = 10
Both_White = 80 

#Värde på hastigheten på roboten(antar mm/s)
Drive_Speed = 50

#Oändlig loop
while True:
    #uppdatering av sensorernas värde samt summa av dem
    rsensor = right_sensor.reflection()
    lsensor = left_sensor.reflection()
    color = color_sensor.color()
    both_sensor = rsensor + lsensor
    print(color) 
    print(deposit)   
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
        print("ngt konstigt")
        pickup = 0

    if deposit==4:
        Drive_Speed=0
        deposit = 0
        print("hej")
        #kör tills trycksensor trycks åt?
        #sedan gör den ngn sekvens så den kommer rätt med gatesen
        #-> till nästa ifsats för att släppa bollar
        #if satser med 3 olika färgena som öppnar rätt gate beroende på färg
        if lastcolor == Color.BLUE:
            #blå öppna gate 1
            gate_small_medium.run_target(90, -90)
            gate_small_medium.run_target(90, 0)
            print("blå")
        elif color == Color.GREEN:
            #grön öppna gate 2
            print("grön")
        elif lastcolor == Color.RED:
            gate_small_medium.run_target(90, -90)
            gate_small_medium.run_target(90, 0)
            print("röd")
        pickup +=1
        wait(10000000)
        #här ksk vi ska ha en variabel som adderas med 1 och när den varit på alla 3
        #så åker den tillbaka till upplockaren?
    elif color in POSSIBLE_COLORS and turn_crossection == 4:
        #300 mm 90 grader 3 sekunder
        robot.drive_time(100, 0, 1000)
        robot.drive_time(50, -90, 1500)
        deposit +=1
        turn_crossection = -1
        print("sväng")
    elif color in POSSIBLE_COLORS and deposit ==3:
        deposit+=1
        lastcolor = color
    elif color in POSSIBLE_COLORS:
        deposit +=1
        robot.drive_time(30, 0, 1000)
    elif color == Color.YELLOW and turn_crossection ==2:
        turn_crossection +=1
        robot.drive_time(30, -45, 500)
    elif color == Color.YELLOW:
        turn_crossection += 1
        robot.drive_time(30, 0, 1000)
        print("addera gul")
    elif both_sensor > Both_White:
        turn_rate = 0
    elif rsensor < Black:
        turn_rate = 150
        print("höger")
    elif lsensor < Black:
        turn_rate = -150
        print("vänster")
    else:
        turn_rate = 0
    
    robot.drive(Drive_Speed, turn_rate)
    