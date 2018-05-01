time = int(input("Please write todays date, scrunch it together"))
birth = int(input("Now, may I ask your birthday?"))

year = time//10000
date = time%10000
day = date//100
month = date%100

year2 = birth//10000
date2 = birth%10000
day2 = date2//100
month2 = date2%100

print("Today's date is", day, "/", month, "/", year)
print("And here is your birthday", day2, "/", month2, "/", year2, "/")

x =(365*year)+(30*month)+day
y =(365*year2)+(30*month2)+day2

total = x-y

year3 = total//365
rem = total%365
month3 = rem//30
day3 = rem%30

print("this is the total time you have been alive", year3, "years", month3, "months and", day3, "days")
