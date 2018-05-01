number = int(input("Please enter a number:"))

for x in range (1, number+1):
    blank = " "
    for y in range(1, x+1):
        blank += str(y)
    print(blank)




