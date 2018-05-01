quar = int(input("How many quarters do you have?"))
dime = int(input("How many dimes?"))
nick = int(input("Nickels?"))
penn = int(input("And finally pennies?"))

total = (quar*0.25)+(dime*0.1)+(nick*0.05)+(penn*0.01)

doll = int(total*100)//100
cent = int(total*100)%100

print("This is the total money you have:", doll, "dollars and", cent, "cents")
