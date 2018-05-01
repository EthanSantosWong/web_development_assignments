number = int(input("Please input a number for how long the sequence will be:"))

stopper = 1

print("This sequence is made via a While Loop.")

while stopper <= number:
    print(stopper*2)
    stopper += 1

print("")

print("This sequence is made via a For Loop.")
for stopper in range(1, number+1):
    print(stopper*2)
    stopper += 1
