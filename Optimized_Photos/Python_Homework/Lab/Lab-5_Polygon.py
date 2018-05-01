import turtle

sides = int(input("Please enter a number of sides:"))

angle = (sides - 2)*180

turns = 180-(angle/sides)

for x in range (1, sides+1):
    turtle.forward(100)
    turtle.left(turns)
    turtle.done
