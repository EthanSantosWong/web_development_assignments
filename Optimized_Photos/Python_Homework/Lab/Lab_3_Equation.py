a = int(input("Please enter a value for a."))
b = int(input("Please enter a value for b."))

if (a==0 and b!=0):
    print("I am sorry, but there is no solution.")
elif (a==0 and b==0):
    print("Goodness, there are infinitely many solutions to this problem.")
else:
    x = (-b)/a
    print("This euation has a single solution to it and it is x=",x)
