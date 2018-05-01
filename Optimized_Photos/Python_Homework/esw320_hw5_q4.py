char = str(input("please input a word:"))
vowels = "aeiou"

found = False

vowel = 0
cons = 0


for letter in char:
    for vow in vowels:
        if letter == vow:
            found = True
            break
    if found == True:
        vowel += 1
    else: cons += 1

    found = False
                
print("Your word has", vowel, "vowels, and", cons, "consonants.")
