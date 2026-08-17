def ft_water_reminder():
    water_day = int(input("Days since last watering: ")) 
    if water_day > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")