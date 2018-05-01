import math

#a = 150.0
#b = 200.0

#anglec = math.degrees(2.0944)

#anglec = math.radians(120)

#anglec = math.radians(2.0944)


#c = math.sqrt(a*a + b*b - (2*a*b + (math.cos(anglec))))

#print (c)

#print(math.cos(anglec))
#print(math.degrees(anglec))

#print(math.radians(120))
#print(math.degrees(120))
#print(math.degrees(2.0944))

#anglea = math.asin((a* math.sin(anglec) ) /c)
#angleb = 180 - (anglec + anglea)

#print(c, anglea, angleb)


b = 150

c = 200

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


C = 180 - 120 - B

print("This should be the final angle:", C)
