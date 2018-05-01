number1 = int(input("Please enter a number:"))
number2 = int(input("Please enter another number:"))
hamm = 0

for x in range (len(str(number1))):
    if number1 % 10 != number2 % 10:
        hamm += 1
    number1 //=10
    number2 //=10

print(hamm)
