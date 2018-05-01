year = int(input("Please input a year that is a number of years in the future"))

birth = (1/7)*60*60*24*365
death = (-1/13)*60*60*24*365
immig = (1/35)*60*60*24*365

currb = year*birth
currd = year*death
curri = year*immig

total = currb+currd+curri

pop = int(total+307357870)

print("This is the population after that amount of time", pop)
