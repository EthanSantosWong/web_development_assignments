quest = int(input("How many sides does this shape have?"))

if (quest == 3):
    print("This shape is a triangle.")

elif (quest == 4):
    side = input("Does this shape have equal side?")
    if (side == "Yes"):
        angles = input("Does this shape have 90 degrees for all of its internal angles?")
        if(angles == "Yes"):
            print("This shape is a square.")
        else: print("This shape is a quadrialteral.")
    else: print("This shape is a quadrilateral.")

elif (quest == 5):
    print("This shape is a pentagon.")

else: print("I apologioze, I do not recognize this shape.")
