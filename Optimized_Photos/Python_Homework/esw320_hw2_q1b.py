pound = int(input("Please input your weight in pounds:"))
inch = int(input("Please input your weight in inches:"))

weight = int(pound*0.453592)
height = float(inch*0.0254)
bmi = weight/height**2

print("YOur BMI is:", bmi)
