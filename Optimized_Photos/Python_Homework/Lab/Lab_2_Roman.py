ques = int(input("Please input a number below 100"))
l = ques//50
rem = ques%50
x = rem//10
rem2 = rem%10
v = rem2//5
i = rem2%5

print("Your number in Roman numerals is", "L"*l, "X"*x, "V"*v, "I"*i)
