#!/usr/bin/env pybricks-micropython


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, TouchSensor, UltrasonicSensor
#from ev3dev2.motor import MoveTank
from pybricks.parameters import Port, Color
from pybricks.robotics import DriveBase
from pybricks.tools import wait
from pybricks.messaging import BluetoothMailboxServer, TextMailbox
# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

#Motorer
left_motor = Motor(Port.B)
right_motor = Motor(Port.A)
gate_big = Motor(Port.C)
gate_medsmall = Motor(Port.D)

#Färgsensorer
right_sensor = ColorSensor(Port.S2)
left_sensor = ColorSensor(Port.S3)
color_sensor = ColorSensor(Port.S1)
#Trycksensor
#touch_sensor = TouchSensor(Port.S4)
ultrasonic_sensor = UltrasonicSensor(Port.S4)

#Bluetooth
#server = BluetoothMailboxServer()
#bluetot = LogicMailbox(name, server)

#Gör så att båda motorerna kan gå samtidigt
robot = DriveBase(left_motor, right_motor, wheel_diameter=75.5, axle_track=104)
#tank_pair = MoveTank(left_motor, right_motor)

#Värden på färgena + sätter in färger
POSSIBLE_COLORS = [Color.RED, Color.GREEN, Color.BLUE, Color.WHITE]
Black = 17
Brown = 35
#på linjen =7
#sensorerna rakt på linjen =31


#Värde på hastigheten på roboten(antar mm/s)
Drive_Speed = 40
turn_rate = 0
turn_crossection = 3
deposit = 1
pickup = 0
beenyellow = False

#Oändlig loop
while True:
    rsensor = right_sensor.reflection()
    lsensor = left_sensor.reflection()
    color = color_sensor.color()
    ultrasensor = ultrasonic_sensor.distance()
    print("distance")
    print(ultrasensor)
    if deposit >= 4:
        #Nollställer värden för att den ska stå still
        #Väntar en sekund och läser av färgen igen för att va helt säker att den läst av rätt ^^
        Drive_Speed=5
        turn_rate = 0
        robot.drive(Drive_Speed, turn_rate)
        #wait(1000)
        dropcolor1 = color_sensor.color()
        #wait(1000)
        dropcolor2 = color_sensor.color()
        #wait(1000)
        dropcolor3 = color_sensor.color()
        dropcolor4 = color_sensor.color()
        dropcolor5 = color_sensor.color()
        dropcolor6 = color_sensor.color()
        dropcolor7 = color_sensor.color()
        dropcolor8 = color_sensor.color()
        dropcolor9 = color_sensor.color()
        dropcolor10 = color_sensor.color()
        dropcolor11 = color_sensor.color()
        dropcolor12 = color_sensor.color()
        dropcolor13 = color_sensor.color()
        dropcolor14 = color_sensor.color()
        dropcolor15 = color_sensor.color()
        dropcolor16 = color_sensor.color()
        dropcolor17 = color_sensor.color()
        dropcolor18 = color_sensor.color()
        dropcolor19 = color_sensor.color()
        dropcolor20 = color_sensor.color()
        while dropcolor1 and dropcolor2 and dropcolor3 and dropcolor4 and dropcolor5 and dropcolor6 and dropcolor7 and dropcolor8 and dropcolor9 and dropcolor10 and dropcolor11 and dropcolor12 and dropcolor13 and dropcolor14 and dropcolor15 and dropcolor16 and dropcolor17 and dropcolor18 and dropcolor19 != dropcolor20:
            #wait(1000)
            dropcolor1 = color_sensor.color()
            #wait(1000)
            dropcolor2 = color_sensor.color()
            #wait(1000)
            dropcolor3 = color_sensor.color()
            dropcolor3 = color_sensor.color()
            dropcolor4 = color_sensor.color()
            dropcolor5 = color_sensor.color()
            dropcolor6 = color_sensor.color()
            dropcolor7 = color_sensor.color()
            dropcolor8 = color_sensor.color()
            dropcolor9 = color_sensor.color()
            dropcolor10 = color_sensor.color()
            dropcolor11 = color_sensor.color()
            dropcolor12 = color_sensor.color()
            dropcolor13 = color_sensor.color()
            dropcolor14 = color_sensor.color()
            dropcolor15 = color_sensor.color()
            dropcolor16 = color_sensor.color()
            dropcolor17 = color_sensor.color()
            dropcolor18 = color_sensor.color()
            dropcolor19 = color_sensor.color()
            dropcolor20 = color_sensor.color()
        
        dropcolor = dropcolor20
        
        #Sätter deposit till 1 eftersom den kommer svänga en gång(+2) och läsa av en färg en gång(+1)
        deposit = 1

        #Sätter turn_crossection till 3 för att den ska svänga nästa gång den läser av en gul färg
        turn_crossection = 3

        #Sekvens där roboten åker fram 320 mm för att inte missa avlastningen av bollarna
        robot.straight(320)
        wait(2000)

        print("avlastning:")
        print(dropcolor10)

        if beenyellow == True:
            #if satser med 3 olika färgena som öppnar rätt gate beroende på färg
            if dropcolor == Color.BLUE:
                #färg 1 öppna gate 1 minsta
                gate_big.run_target(90, 90)
                wait(1000)
                gate_big.run_target(90, 0)
                print("Blå")
            elif dropcolor == Color.RED:
                #färg 2 öppna gate 2 mellersta
                gate_medsmall.run_target(90, -90)
                wait(1000)
                gate_medsmall.run_target(90, 0)
                print("röd")
            elif dropcolor == Color.WHITE:
                #färg 3 öppna gate 3 största bollarna
                gate_medsmall.run_target(90, 90)
                wait(1000)
                gate_medsmall.run_target(90, 0)
                print("vit")
        

        print("avlastning efter:")
        print(dropcolor)
        #Adderar pickup med 1 varje deposit(pickup=3 -> whileloop som åker och plockar upp nya bollar)
        pickup +=1
        wait(1000)

        #Sekvens som backar tillbacks roboten och sen gör en 180-sväng(260 är en konstig felfaktor men den svänger 180)
        robot.straight(-360)
        wait(1000)
        robot.turn(360)
        wait(1000)
        
        Drive_Speed = 40
        #Framtiden kan en failsafe i form av en whileloop skapas för att hitta den svarta färgen
    elif color in POSSIBLE_COLORS and deposit ==3:
        deposit+=1
    elif color in POSSIBLE_COLORS and turn_crossection >= 4:
        #Sekvens för sväng kan behövas finjusteras men den funkar atm
        #test ^^
        robot.drive_time(32, 0, 800)

        robot.drive_time(75, 0, 1100)
        robot.drive_time(70, 110, 1620)
        robot.drive_time(60, 0, 1900)

        
        deposit +=2
        turn_crossection = 0
        beenyellow = False
        print("sväng:")
        print(color)
    elif color in POSSIBLE_COLORS:
        deposit +=1
        #Sekvens så att färgsensr åker förbi tejpen och inte läser av den igen
        robot.drive_time(32, 0, 800)
    elif color == Color.YELLOW:
        turn_crossection += 1
        beenyellow = True
        #Sekvens så att färgsensr åker förbi tejpen och inte läser av den igen
        robot.drive_time(32, 0, 800)
    elif rsensor < Black:
        turn_rate = 50
        #print("höger")
    elif lsensor < Black:
        turn_rate = -50
        #print("vänster")
    else:
        turn_rate = 0

    
    robot.drive(Drive_Speed, turn_rate)
    
    

    

    

    
    

