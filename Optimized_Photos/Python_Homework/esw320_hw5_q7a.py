roman = str(input("Plese input a simplified roman numeral number:"))

numeral = "MDCLXVI"

total = 0

for letter in roman:
    print(letter)

    if letter == "M":
        total += 1000
    elif letter == "D":
        total += 500
    elif letter == "C":
        total += 100
    elif letter == "L":
        total += 50
    elif letter == "X":
        total += 10
    elif letter == "V":
        total += 5
    elif letter == "I":
        total += 1
    
print("This is the number:", total)
