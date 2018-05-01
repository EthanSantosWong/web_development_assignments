phrase = str(input("Please type out a phase that has an odd amount of characters, spaces count too."))


print("This is the middle chracter:", phrase[len(phrase)//2:len(phrase)//2+1])
print("This is the first half:", phrase[:len(phrase)//2])
print("This is the latter half:", phrase[len(phrase)//2+1:])
