import random
number = random.randint(1, 100)
print("There is a number between 1 and 100.")
print("This is a cheat sheet.", number)

guess = 0

while guess != number:
    guess = int(input("Guess what that number is:"))

    if guess == number:
        print("You did it! You won!")
    elif guess > number:
        print("Sorry, but the number is larger than your guess. Try again:")
    elif guess < number:
        print("Sorry, but the number is smaller than your guess. Try again:")
    
