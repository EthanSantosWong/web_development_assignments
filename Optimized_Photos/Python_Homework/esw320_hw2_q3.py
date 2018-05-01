import math
import turtle

b = int(input("Please input a number for a triangle side:"))

c = int(input("Please input a number for another triangel side:"))

Aan = int(input("Please input an angle for the tirangle:"))

A = math.radians(120)

a = int(math.sqrt(b**2 + c**2 - 2*b*c*math.cos(A)))

print("The value of the third side is:", a)


#Given: side b = 150, side a = X and angle A = 120°. Angle B is desired.

#sin B / 150 = sin A / X

Z = 2*a*c

Y = (a**2 + c**2 - b**2)

print ("Z= ",Z)
print ("Y= ",Y)

Bcal = math.acos( Y / Z)

B = math.degrees(Bcal)

#B = math.asin(b*(math.sin(120)/a))

print("The angle value of B is:", B)


C = 180 - Aan - B

print("This should be the final angle:", C)

angleA = 180-Aan
angleB = 180-B
angleC = 180-C

turtle.forward(b)
turtle.left(angleA)
turtle.forward(c)
turtle.left(angleB)
turtle.forward(a)
turtle.left(angleC)




