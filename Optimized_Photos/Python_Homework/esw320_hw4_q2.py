number = int(input("Please give a number for how big this hourglass will be."))

pencil = number

draw = number

#for draw in range (number, 0, -1):
    #print("*", end=" ") 
    #draw -= 1


#while pencil <= number:
    #print(pencil*2-1)
    #pencil -=1
    #if (pencil == 0):
        #break

for pencil in range (number, 0,-1):
    for draw in range (pencil, 0, -1):
        draw == draw*2-1
        print("*", end=" ") 
        draw -= 1
    print("Good day")
    pencil -= 1

for pencil in range (1, number+1,):
    for draw in range (pencil, 0, -1):
        draw == draw*2-1
        print("*", end=" ") 
        draw -= 1
    print("Hello")
    pencil -= 1
