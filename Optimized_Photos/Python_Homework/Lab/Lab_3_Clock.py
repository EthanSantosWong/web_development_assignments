time = int(input("Please input the time in Military Time."))

if (time//100 == 0):
    hour = 00

elif (time//100 >12):
    hour = (time//100)-12

else: hour = time//100


minute = time%100

if (hour <= 12):
    day = "PM"
else: day = "AM"

print(time, "in standard format is", hour,":", minute, day)
