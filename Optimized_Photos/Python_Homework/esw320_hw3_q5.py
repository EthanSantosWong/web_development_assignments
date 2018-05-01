print("Please enter three sides of a triangle.")
side1 = int(input("What is the length of the first side?"))
side2 = int(input("What is the length of the seconds side?"))
side3 = int(input("What is the length of the final side? allow this to be the hypotenuse."))

if (side1 == side2 == side3):
    print(side1, side2,"and", side3, "produce an equilateral triangle.")

elif (side1 == side2 != side3):
    if (side1**2 + side2**2 == side3**2):
        print(side1, side2, "and", side3, "produce an isoscles right triangle.")
    else: print(side1, side2,"and", side3, "produce an isosclese triangle.")

elif (side1**2 + side2**2 == side3**2):
    print(side2, side2, "and", side3, "produce a right triangle.")

else: print(side1, side2, "and", side3, "produce a triangle that is neiter equilateral or isosceles.")
