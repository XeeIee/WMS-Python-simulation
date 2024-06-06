from time import sleep
from random import randint
#library

Loading = randint(5,20)
Loading1 = randint(5,10)
Core_Temp = 457
Core_Damage = 0
Core_Status = (100-Core_Damage)
Oil = 2.5
Cooldown = randint(100, 175)
wd_total = 30
wd_in_area = 3
corpses_in_area = 0
#Variables

if Core_Temp < 0:
    Core_Temp = 0

def Status():
    sleep(0.2)
    print("CORE STATUS:", Core_Status)
    sleep(0.2)
    print("CORE_TEMP:", Core_Temp)
    if Core_Temp >= 300:
        sleep(1)
        print("CRITICAL")
        sleep(0.9)
    else:
        sleep(0.2)
    
    sleep(0.2)
    print("OIL:", Oil,"L")
    sleep(0.2)

print("Booting up//")
sleep(0.5)
print("Exposition//")
sleep(Loading)
print("Successfully loaded")
#sleep(Loading)
#Flavour booting sequence

print("--------------------------------------------------------------------------------")
sleep(0.1)
print("Welcome back")
sleep(1)
print("Data limited")
sleep(1)
print("Core_Temp > 400C")
sleep(2)
print("Please find sustainable oil source to prevent overheat")
sleep(2)
Command_Tutorial = input("Refresh Commands?(Y/N)")
Command_Tutorial = Command_Tutorial.lower()
#Set up

if Command_Tutorial == "y":
    print("Loading..")
    sleep(Loading1)
    print("Commands found")
    sleep(3)
    print("Consume: Use a Litre of oil from within your storage")
    sleep(0.3)
    print("Fly: Find new location in search of Worker Drones.")
    sleep(0.3)
    print("Extract: Take oil from worker corpses in order to fill your oil tank")
    sleep(0.3)
    print("Disassemble: Kill Worker Drones, if there are any within the area")
    sleep(0.3)
    print("Status: Check Core Status, Core temp, and Oil Tank.")
    sleep(0.3)
    print("Boot: You're done with endless worker murder, time to log off.")
    sleep(1)
    print("Great, now let's play.")
    sleep(3)

elif Command_Tutorial == "N" or Command_Tutorial == "n":
    print("As you wish, let's eat.")
    sleep(3)

else:
    #break
    print("break")

#optional tutorial
while wd_total > 0:
    Action = input("Awaiting command input:")
    Action = Action.lower()
    #game begins  
    
    if Action == "status":
        Status()
    #status command

    elif Action == "kill":
        wd_total = wd_total-5
        sleep(0.1)
        print("You killed the worker!!! current workers alive:", wd_total)
        sleep(0.1)
    #kill admin command

    elif Action == "consume":
        print("Consuming oil in oil tank..")
        sleep(Loading1)
        if Oil > 1:
            Oil = Oil-1
            Core_Temp = Core_Temp-Cooldown
            print("Oil consumed!")
            sleep(1)
            print("You have ", Oil ,"L left.")
            sleep(1)
        else:
            print("Insufficient Oil, find more oil.")
            sleep(2)

    
    else:
        #break
        print("Not a command bud.")

print("All Worker Drones disassembled, return to base.")
    
