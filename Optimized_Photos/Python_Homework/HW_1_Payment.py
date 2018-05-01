print("Please enter how many dollars tyou have, then how much cents are two seperate lines.")
doll = int(input())
cent = int(input())

total = (doll*100)+cent

quar = total//25
rem = total%25
dime = rem//10
rem2 = rem%10
nick = rem2//5
penn = rem2%5

print("Your total is", doll, "dollars and", cent, "cents")
print("Which is",quar, "quarters,",dime,"dimes,",nick,"nickels and",penn,"pennies.") 
