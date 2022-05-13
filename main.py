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
#SERVER = 'ev3dev'
"""
print('waiting for connection...')
server.wait_for_connection()
print('connected!')
"""
#bluetot = LogicMailbox(name, server)

#Gör så att båda motorerna kan gå samtidigt
robot = DriveBase(left_motor, right_motor, wheel_diameter=75.5, axle_track=104)
#tank_pair = MoveTank(left_motor, right_motor)

#Värden på färgena + sätter in färger
POSSIBLE_COLORS = [Color.RED, Color.GREEN, Color.BLUE, Color.WHITE]
Black = 16
Brown = 35
#på linjen =7
#sensorerna rakt på linjen =31


#Värde på hastigheten på roboten(antar mm/s)
Drive_Speed = 40
turn_rate = 0
turn_crossection = 3
deposit = 1
pickup = 0
sv = 0
turn = "left"
beenyellow = False
idle = False
#Oändlig loop
while True:
    rsensor = right_sensor.reflection()
    lsensor = left_sensor.reflection()
    color = color_sensor.color()
    #ultrasensor = ultrasonic_sensor.distance()
    print("höger:")
    print(rsensor)
    print("vänster")
    print(lsensor)



    while pickup >=3:
        rsensor = right_sensor.reflection()
        lsensor = left_sensor.reflection()
        color = color_sensor.color()
        ultrasensor = ultrasonic_sensor.distance()
        #print(ultrasensor)
        #print("höger:")
        #print(rsensor)
        #print("vänster")
        #print(lsensor)
        if ultrasensor <= 195:
            #sekvens vid upphämtning av bollar
            Drive_Speed = 0
            turn_rate = 0
            robot.drive_time(200, 0, 3000)
            wait(3000)
            robot.drive_time(-300, 0, 2000)
            
            #failsafe ksk
            robot.drive_time(180, 0, 1100)
            robot.turn(-160)
            #reset values
            pickup=0
            Drive_Speed = 40
            turn_rate = 0
            turn_crossection = 3
            deposit = 1
            pickup = 0
            beenyellow = False
            idle = False
        elif color in POSSIBLE_COLORS and turn_crossection >= 4 and idle == False:
            #Sekvens för sväng kan behövas finjusteras men den funkar atm
            #test ^^
            robot.drive_time(35, 0, 800)

            #Failsafe
            k = 1
            turnkonst = 0
            sv = 0
            lastcolor = color_sensor.color()
            while lastcolor != Color.BLACK:
                if sv >=2:
                    robot.straight(20)
                    sv = 0
                turnkonst += 5
                robot.turn(-5*k)
                lastcolor = color_sensor.color()
                if turnkonst == 80:
                    robot.turn(80*k)
                    k *= -1
                    turnkonst = 0
                    sv +=1

            robot.turn(-15*k)

            #Svängsekvens
            robot.drive_time(200, 0, 1100)
            robot.turn(-160)
            robot.drive_time(100, 0, 1200)
            robot.turn(350)
            

            #Failsafe
            k = -1
            turnkonst = 0
            sv = 0
            lastcolor = color_sensor.color()
            while lastcolor != Color.BLACK:
                if sv >=2:
                    robot.straight(20)
                    sv=0
                turnkonst += 5
                robot.turn(-5*k)
                lastcolor = color_sensor.color()
                if turnkonst == 80:
                    robot.turn(80*k)
                    k *= -1
                    turnkonst = 0
                    sv += 1

            idle = True
            Drive_Speed = 0
            turn_rate = 0
            turn_crossection = 0
            print("sväng:")
            print(color)
        elif color == Color.YELLOW and idle == False:
            turn_crossection += 1
            #Sekvens så att färgsensr åker förbi tejpen och inte läser av den igen
            robot.drive_time(32, 0, 800)
            
            #Failsafe
            k = 1
            turnkonst = 0
            sv = 0
            lastcolor = color_sensor.color()
            while lastcolor != Color.BLACK:
                if sv >=2:
                    robot.straight(20)
                    sv=0
                turnkonst += 5
                robot.turn(-5*k)
                lastcolor = color_sensor.color()
                if turnkonst == 80:
                    robot.turn(80*k)
                    k *= -1
                    turnkonst = 0
                    sv += 1
        elif rsensor < Black and idle == False:
            #turn_rate = 50
            print("höger")
            
            turn_rate = ((Black-rsensor)*5 + 40)
            print(turn_rate)
        elif lsensor < Black and idle == False:
            #turn_rate = -50
            print("vänster")
            
            turn_rate = -((Black-lsensor)*5 + 40)
            print(turn_rate)
        else:
            turn_rate = 0

    
        robot.drive(Drive_Speed, turn_rate)













    if deposit >= 4:
        #Nollställer värden för att den ska stå still
        #Väntar en sekund och läser av färgen igen för att va helt säker att den läst av rätt ^^
        Drive_Speed=2
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

        robot.drive_time(32, 0, 800)
        #Failsafe
        k=-1
        turnkonst = 0
        sv = 0
        lastcolor = color_sensor.color()
        while lastcolor != Color.BLACK:
            if sv >=2:
                robot.straight(20)
                sv=0
            turnkonst += 6
            robot.turn(-6*k)
            lastcolor = color_sensor.color()
            #wait(500)
            if turnkonst == 78:
                robot.turn(78*k)
                k *= -1
                turnkonst = 0
                sv += 1
        
        #Sekvens där roboten åker fram 320 mm för att inte missa avlastningen av bollarna
        robot.straight(50)
        #failsafe
        if turn == "right":
            k = -1
        elif turn == "left":
            k = 1
        turnkonst = 0
        sv = 0
        lastcolor = color_sensor.color()
        while lastcolor != Color.BLACK:
            if sv >=2:
                robot.straight(20)
                sv=0
            turnkonst += 6
            robot.turn(-6*k)
            lastcolor = color_sensor.color()
            #wait(500)
            if turnkonst == 78:
                robot.turn(78*k)
                k *= -1
                turnkonst = 0
                sv += 1
        robot.straight(270)
        wait(2000)

        print("avlastning:")
        print(dropcolor20)
        
        if beenyellow == True:
            #if satser med 3 olika färgena som öppnar rätt gate beroende på färg
            if dropcolor == Color.BLUE:
                #färg 1 öppna gate 1 stora bollar
                gate_big.run_target(90, 90)
                wait(1000)
                #wiggle wiggle
                robot.straight(30)
                robot.straight(-30)
                robot.straight(30)
                robot.straight(-30)
                robot.straight(30)
                robot.straight(-30)
                
                wait(1000)
                gate_big.run_target(90, 0)
                print("Blå")
            elif dropcolor == Color.GREEN:
                #färg 2 öppna gate 2 mellersta
                gate_medsmall.run_target(60, -60)
                wait(1000)
                #wiggle wigglerobot.straight(30)
                robot.straight(-30)
                robot.straight(30)
                robot.straight(-30)
                robot.straight(30)
                robot.straight(-30)
                wait(1000)
                gate_medsmall.run_target(60, 0)
                print("grön")
            elif dropcolor == Color.WHITE:
                #färg 3 öppna minsta bollarna
                gate_medsmall.run_target(60, 60)
                wait(1000)
                #wiggle wiggle
                robot.straight(30)
                robot.straight(-30)
                robot.straight(30)
                robot.straight(-30)
                robot.straight(30)
                robot.straight(-30)
                wait(1000)
                gate_medsmall.run_target(60, 0)
                print("vit")
        
        
        print("avlastning efter:")
        print(dropcolor20)
        #Adderar pickup med 1 varje deposit(pickup=3 -> whileloop som åker och plockar upp nya bollar)
        pickup +=1
        wait(1000)

        #Sekvens som backar tillbacks roboten och sen gör en 180-sväng(260 är en konstig felfaktor men den svänger 180)
        robot.straight(-330)
        wait(1000)
        robot.turn(350)
        wait(1000)

        #Failsafe
        if turn == "right":
            k = -1
        elif turn == "left":
            k = 1
        turnkonst = 0
        sv = 0
        lastcolor = color_sensor.color()
        while lastcolor != Color.BLACK:
            if sv >=2:
                robot.straight(20)
                sv=0
            turnkonst += 6
            robot.turn(-6*k)
            lastcolor = color_sensor.color()
            #wait(500)
            if turnkonst == 120:
                robot.turn(120*k)
                k *= -1
                turnkonst = 0
                sv += 1
        
        Drive_Speed = 40
        #Framtiden kan en failsafe i form av en whileloop skapas för att hitta den svarta färgen
    elif color in POSSIBLE_COLORS and deposit ==3:
        deposit+=1
        #robot.drive_time(32, 0, 800)
    elif color in POSSIBLE_COLORS and turn_crossection >= 4:
        #Sekvens för sväng kan behövas finjusteras men den funkar atm
        #test ^^
        robot.drive_time(35, 0, 800)

        #Failsafe
        if turn == "right":
            k = -1
        elif turn == "left":
            k = 1
        turnkonst = 0
        sv = 0
        lastcolor = color_sensor.color()
        while lastcolor != Color.BLACK:
            if sv >=2:
                robot.straight(20)
                sv = 0
            turnkonst += 6
            robot.turn(-6*k)
            lastcolor = color_sensor.color()
            #wait(500)
            if turnkonst == 84:
                robot.turn(84*k)
                k *= -1
                turnkonst = 0
                sv +=1

        robot.turn(-15*k)
        #Svängsekvens
        robot.drive_time(200, 0, 1100)
        robot.turn(160)

        #Failsafe
        k=-1
        turnkonst = 0
        sv = 0
        lastcolor = color_sensor.color()
        while lastcolor != Color.BLACK:
            if sv >=2:
                robot.straight(20)
                sv = 0
            turnkonst += 6
            robot.turn(-6*k)
            lastcolor = color_sensor.color()
            #wait(500)
            if turnkonst == 84:
                robot.turn(84*k)
                k *= -1
                turnkonst = 0
                sv +=1

        #Reset values
        deposit +=1
        turn_crossection = 0
        beenyellow = False
        print("sväng:")
        print(color)
    elif color in POSSIBLE_COLORS:
        deposit +=1
        #Sekvens så att färgsensr åker förbi tejpen och inte läser av den igen
        robot.drive_time(40, 0, 800)

        #Failsafe
        if turn == "right":
            k = -1
        elif turn == "left":
            k = 1
        turnkonst = 0
        sv = 0
        lastcolor = color_sensor.color()
        while lastcolor != Color.BLACK:
            if sv >=2:
                robot.straight(20)
                sv=0
            turnkonst += 6
            robot.turn(-6*k)
            lastcolor = color_sensor.color()
            #wait(500)
            if turnkonst == 84:
                robot.turn(84*k)
                k *= -1
                turnkonst = 0
                sv += 1
    elif color == Color.YELLOW:
        turn_crossection += 1
        beenyellow = True
        #Sekvens så att färgsensr åker förbi tejpen och inte läser av den igen
        robot.drive_time(32, 0, 800)

        #Failsafe
        if turn == "right":
            k = -1
        elif turn == "left":
            k = 1
        turnkonst = 0
        sv = 0
        lastcolor = color_sensor.color()
        while lastcolor != Color.BLACK:
            if sv >=2:
                robot.straight(20)
                sv=0
            turnkonst += 6
            robot.turn(-6*k)
            lastcolor = color_sensor.color()
            #wait(500)
            if turnkonst == 84:
                robot.turn(84*k)
                k *= -1
                turnkonst = 0
                sv += 1
    elif rsensor < Black:
        turn_rate = ((Black-rsensor)*6 + 40)
        turn = "right"
        #print("höger")
    elif lsensor < Black:
        turn_rate = -((Black-lsensor)*6 + 40)
        turn = "left"
        #print("vänster")
    else:
        turn_rate = 0

    
    robot.drive(Drive_Speed, turn_rate)
    
    

    

    

    
    

