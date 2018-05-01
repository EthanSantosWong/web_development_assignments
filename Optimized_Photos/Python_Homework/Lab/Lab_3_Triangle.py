a = int(input("Please enter a leg measurement of a triangle:"))
b = int(input("Please enter another leg measurement of that triangle:"))
c = int(input("Please enter the hypothenuse measurement of that triangle:"))

if (a**2+b**2 == c**2):
    print("These three sides form a right trangle.")
else: print("These three side measurements do not form a right triangle.")
