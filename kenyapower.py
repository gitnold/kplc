#A python program to calculate power consumption of home appliances
import pendulum
from faker import Faker
import pandas as pd
from datetime import datetime
sample = Faker()
sample.time()

class Kenyapower():
    def __init__(self):
        global ratingac, computers, cleaning, kitchen, livingroom, init, kwh
        unit = "1 Kwh"
        kwh = "1000 watts"
        ratingac = "RoomAc : 1000w \nCentral Ac : 2000w"
        computers = "\n\nLaptop : 50w \nDesktopPc : 200w \nprinter : 100w"
        cleaning = "\n\nwashingmachine : 500w \nVacuumcleaner(upright) : 700 \nVacuumcleaner(Hand) : 150 \nDishwasher : 1200w"
        kitchen = "\n\nBlender : 300w \nCoffeemaker : 800 \nRefrigerator : 60w per hour \nElectric cooker : 2000w \nMicrowave : 200w \nToaster : 100w"
        livingroom = "\n\nTv : 100w \nsoundsystem : 80w \nWifi : 60w \nsatelitedish : 30w"
    def welcome(self):
        print("Welcome to Smartpower portal\nENTER OPTION[1.Smartmeter, 2.Enter token]")
        option = int(input("Enter option number : ")) 
        if option == 1:
            power.metprompt() 
        elif option == 2:
            power.tokprompt()
        else:
            print("Invalid option!") 
    def tokprompt(self):
        token = str(input("Enter token no[24 digits] : "))
        tlen = len(token)
        if tlen == 24:
            print("Token recharge succeessful!")
        else:
            print("Invalid token!")                          
    def metprompt(self):
        print("Welcome to Smartmeter!\nOPTIONS : 1.View devices, 2.See power consumption stats")
        option = int(input("Enter option number : ")) 
        if option == 1:
            power.view()
        elif option == 2:
            power.stats()
        else:
            print("Invalid option!")
            power.welcome() 
    def view(self):
         print("POWER RATING OF COMMON HOME APPLIANCES IN WATTS!")
         print(ratingac, computers, cleaning, kitchen, livingroom)        
    def stats(self):
        print("WELCOME TO DEVICE STATS!")
        power.category()
    def category(self):
        devices = {'\n\nDesktopPc' : 200, 'washingmachine' : 500, 'Refrigerator' : 60, 'Tv' : 100, 'soundsystem' : 80, 'Wifi' : 60, 'satelitedish' : 30}
        powerrate = 200,500,60,100,80,60,3
        time = datetime.now()
        ct = time.strftime('%H:%M:%S')
        t1 = datetime.strptime(ct, "%H:%M:%S")
        for v in devices:
            ontime = str(sample.time())
            t2 = datetime.strptime(ontime, "%H:%M:%S")
            runtime = t1 - t2
            sec = runtime.total_seconds()
            hrs = sec / 3600
            for power in powerrate:    
                units = int(hrs * power)             
            print(v,       "[POWER USAGE IN WATTS] : ",          abs(units))
        
power = Kenyapower()
power.welcome()            