char = str(input("Please type a single character:"))

asc = ord(char)

print(asc)

if asc in range (33, 48):
    print("This character is not an alphanumeric character.")
    
elif asc in range (48, 58):
    print("This character is a number.")
    
elif asc in range (58, 65):
    print("This character is not an alphanumeric character.")

elif asc in range (65, 91):
    print("This character is a capitol letter.")

elif asc in range (91, 97):
    print("This character is not an alphanumeric character.")

elif asc in range (97, 123):
    print("This character is a lower case letter.")

elif asc in range (123, 127):
    print("This character is not an alphanumeric character.")
