weight = float(input("enter your weight :"))
height = float(input("enter your hight :"))
BMI = weight / (height ** 2)
print("your BMI is :",BMI)

if BMI < 18.5 :
    print("you're underweight !")
elif BMI < 25.5 :
    print("you're normal !")
elif BMI < 30 :
    print("you're overweight !")
else :
    print("obese")