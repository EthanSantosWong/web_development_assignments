number = int(input("Please enter a number:"))

for x in range (1, number+1):
    space = "."
    print(space*(number-x), str(x)*(x))
