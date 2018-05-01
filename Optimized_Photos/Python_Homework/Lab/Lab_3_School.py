name = input("Please state thy name.")
grad = int(input("What is thine graduation year?"))
year = int(input("What, pray tell, is the current year?"))

calc = grad - year

if (calc == 0):
    print(name, "thy doth already graduated, congradulations.")
elif (calc == 1):
    print(name, "thy art a senior, just a tad longer.")
elif (calc == 2):
    print(name, "thy art a junior, time doth flies by.")
elif (calc == 3):
    print(name, "thy art a sophomore, I hope thy art getting the hang of this.")
elif (calc == 4):
    print(name, "thy art a freshman, I wish thine the best of luck.")
else: print(name, "thou art not in college or freshly graduated.")
