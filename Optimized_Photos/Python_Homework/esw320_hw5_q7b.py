number = int(input("Please input a number:"))

calc = number

roman = " "

while calc != 0:

    if calc >= 1000:
        roman += "M"
        calc -= 1000
        
    elif calc >= 500:
        roman += "D"
        calc -= 500
        
    elif calc >= 100:
        roman += "C"
        calc -= 100

    elif calc >= 50:
        roman += "L"
        calc -= 50

    elif calc >= 10:
        roman += "X"
        calc -= 10

    elif calc >= 5:
        roman += "V"
        calc -= 5

    elif calc >= 1:
        roman += "I"
        calc -= 1

    else: break
        

print("This is your roman numeral:", roman)
