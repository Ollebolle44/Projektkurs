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
#Trycksensor
touch_sensor = TouchSensor(Port.S4)

deposit = 1
pickup = 0
turn_crossection = 3
stop = False
pressed = False
pickupballs = False

#Gör så att båda motorerna kan gå samtidigt
robot = DriveBase(left_motor, right_motor, wheel_diameter=75.5, axle_track=104)

#Värden på färgena + sätter in färger
POSSIBLE_COLORS = [Color.RED, Color.GREEN, Color.BLUE]
Black = 10
Both_White = 80 

#Värde på hastigheten på roboten(antar mm/s)
Drive_Speed = 45

#Oändlig loop
while True:
    #uppdatering av sensorernas värde samt summa av dem
    rsensor = right_sensor.reflection()
    lsensor = left_sensor.reflection()
    color = color_sensor.color()
    both_sensor = rsensor + lsensor  


    #While loopen kommer sättas igång när alla bollar lämnats och används för att plocka upp nya
    while pickup >= 3:
       
        rsensor = right_sensor.reflection()
        lsensor = left_sensor.reflection()
        color = color_sensor.color()
        both_sensor = rsensor + lsensor
        pressed = touch_sensor.pressed() 

        if pickupballs == True:
            #sekvens för avlämning av bollar
            print("banab")
            wait(5000)
            print("yes det funkar")
            robot.straight(-100)
            robot.turn(265)
            k = 1
            turnkonst = 0
            lastcolor = color_sensor.color()
            while lastcolor != Color.BLACK:
                turnkonst += 5
                robot.turn(-5*k)
                lastcolor = color_sensor.color()
                wait(500)
                if turnkonst == 120:
                    robot.turn(120)
                    k *= -1
                    turnkonst = 0
            
            
            
            
            pickupballs = False
            pickup = 0
            
            #reset values
            Drive_Speed = 45
            deposit = 1
            pickup = 0
            turn_crossection = 3
            stop = False
        elif pressed == True:
            #sekvens för att stoppa roboten och sedan gå in i första ifsatsen
            Drive_Speed = 0
            turn_rate = 0
            stop = True
            pickupballs = True
        elif color in POSSIBLE_COLORS and turn_crossection == 4:
            robot.drive_time(32, 0, 800)
            k = 1
            turnkonst = 0
            lastcolor = color_sensor.color()
            while lastcolor != Color.BLACK:
                turnkonst += 5
                robot.turn(-5*k)
                lastcolor = color_sensor.color()
                wait(500)
                if turnkonst == 120:
                    robot.turn(120)
                    k *= -1
                    turnkonst = 0

            robot.drive_time(50, 0, 1100)
            robot.drive_time(70, 93, 1620)
            robot.drive_time(60, 0, 1900)


            k = 1
            turnkonst = 0
            lastcolor = color_sensor.color()
            while lastcolor != Color.BLACK:
                turnkonst += 5
                robot.turn(-5*k)
                lastcolor = color_sensor.color()
                wait(500)
                if turnkonst == 120:
                    robot.turn(120)
                    k *= -1
                    turnkonst = 0

            turn_crossection = 0
        elif color in POSSIBLE_COLORS:
            robot.drive_time(28, 0, 800)
        elif color == Color.YELLOW:
            turn_crossection +=1
            robot.drive_time(28, 0, 800)
        elif rsensor < Black and stop == False:
            turn_rate = 100
            print("höger")
        elif lsensor < Black and stop == False:
            turn_rate = -100
            print("vänster")
        else:
            turn_rate = 0

        if stop == False:
            robot.drive(Drive_Speed, turn_rate)
        else:
            robot.drive(0, 0)


        

    #1. Den åkt förbi 4 färger och kommer lämna av en bollsort beroende på den sista färgen
    #2. Den åker förbi en possible color och har 3 i depositvärde och adderar deposit med 1 samt aktiverar stop
    #3. Den åker förbi en av de fyra färgena och svänger till höger(när turn_crossection >=4)
    #4. Den åker förbi en possible color och adderar deposit med 1 och åker förbi tejpen
    #5. Den åker förbi en gul färg och kommer addera turn_crossection med 1 och åker förbi tejpen
    #6. Framtida failsafe
    #7. Höger Sensor ser svart svänger höger
    #8. Vänster Sensor ser svart svänger vänster
    #9. Allt är fine kör rakt
    #If satsen för drivebase är för att den ska stanna när stop = true

    if deposit >= 4 and stop == True:
        #Nollställer värden för att den ska stå still
        #Väntar en sekund och läser av färgen igen för att va helt säker att den läst av rätt ^^
        wait(1000)
        dropcolor = color_sensor.color()

        robot.drive_time(32, 0, 800)
        k = 1
        turnkonst = 0
        lastcolor = color_sensor.color()
        while lastcolor != Color.BLACK:
            turnkonst += 5
            robot.turn(-5*k)
            lastcolor = color_sensor.color()
            wait(500)
            if turnkonst == 120:
                robot.turn(120)
                k *= -1
                turnkonst = 0

        Drive_Speed=0
        turn_rate = 0

        #Sätter deposit till 1 eftersom den kommer svänga en gång(+2) och läsa av en färg en gång(+1)
        deposit = 1

        #Sätter turn_crossection till 3 för att den ska svänga nästa gång den läser av en gul färg
        turn_crossection = 3

        #Sekvens där roboten åker fram 320 mm för att inte missa avlastningen av bollarna
        robot.straight(320)
        wait(2000)

        print("hej")
        #if satser med 3 olika färgena som öppnar rätt gate beroende på färg
        if dropcolor == Color.BLUE:
            #färg 1 öppna gate 1 minsta
            gate_big.run_target(90, 90)
            wait(1000)
            gate_big.run_target(90, 0)
            print("Blå")
        elif dropcolor == Color.RED:
            #färg 2 öppna gate 2 mellersta
            gate_big.run_target(90, -90)
            wait(1000)
            gate_big.run_target(90, 0)
            print("röd")
        elif dropcolor == Color.WHITE:
            #färg 3 öppna gate 3 största bollarna
            gate_small_medium.run_target(90, -90)
            wait(1000)
            gate_small_medium.run_target(90, 0)
            print("vit")
        
        #Adderar pickup med 1 varje deposit(pickup=3 -> whileloop som åker och plockar upp nya bollar)
        pickup +=1
        wait(1000)
        stop = False

        #Sekvens som backar tillbacks roboten och sen gör en 180-sväng(260 är en konstig felfaktor men den svänger 180)
        robot.straight(-360)
        wait(1000)
        robot.turn(265)
        wait(1000)
        
        k = 1
        turnkonst = 0
        lastcolor = color_sensor.color()
        while lastcolor != Color.BLACK:
            turnkonst += 5
            robot.turn(-5*k)
            lastcolor = color_sensor.color()
            wait(500)
            if turnkonst == 120:
                robot.turn(120)
                k *= -1
                turnkonst = 0
            
        
        Drive_Speed = 45
        #Framtiden kan en failsafe i form av en whileloop skapas för att hitta den svarta färgen
    elif color in POSSIBLE_COLORS and deposit ==3 and stop == False:
        deposit+=1
        lastcolor = color
        stop = True
    elif color in POSSIBLE_COLORS and turn_crossection >= 4 and stop == False:
        #Sekvens för sväng kan behövas finjusteras men den funkar atm
        #test ^^
        robot.drive_time(32, 0, 800)
        k = 1
        turnkonst = 0
        lastcolor = color_sensor.color()
        while lastcolor != Color.BLACK:
            turnkonst += 5
            robot.turn(-5*k)
            lastcolor = color_sensor.color()
            wait(500)
            if turnkonst == 120:
                robot.turn(120)
                k *= -1
                turnkonst = 0

        robot.drive_time(50, 0, 1100)
        robot.drive_time(70, 93, 1620)
        robot.drive_time(60, 0, 1900)

        k = 1
        turnkonst = 0
        lastcolor = color_sensor.color()
        while lastcolor != Color.BLACK:
            turnkonst += 5
            robot.turn(-5*k)
            lastcolor = color_sensor.color()
            wait(500)
            if turnkonst == 120:
                robot.turn(120)
                k *= -1
                turnkonst = 0

        deposit +=2
        turn_crossection = 0
        print("sväng")
    elif color in POSSIBLE_COLORS and stop == False:
        deposit +=1
        #Sekvens så att färgsensr åker förbi tejpen och inte läser av den igen
        robot.drive_time(28, 0, 800)
    elif color == Color.YELLOW and stop == False:
        turn_crossection += 1
        #Sekvens så att färgsensr åker förbi tejpen och inte läser av den igen
        robot.drive_time(28, 0, 800)
    elif rsensor < Black and stop == False:
        turn_rate = 100
        print("höger")
    elif lsensor < Black and stop == False:
        turn_rate = -100
        print("vänster")
    else:
        turn_rate = 0
    
    if stop == False:
        robot.drive(Drive_Speed, turn_rate)
    else:
        robot.drive(0, 0)

