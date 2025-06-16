#Write a program to check whether the given values have boolean values or not.
variable1=1
variable2=2
variable3=3
if variable1 and variable2 and variable3:
    print(True)
else:
    print(False)

var1=-4
var2=0
var3=5
if var1 or var2 or var3:
    print(True)
else:
    print(False)

num1=int (input("Choose a first number"))
num2=int (input("Choose a second number"))
num3=int (input("Choose a third number"))
if num1>0 or num2>0 or num3>0:
    print("At least one of your numbers were greater than zero")
else:
    print("All of your numbers were less than one")

#Write a program to check the application of not equal operator
text="banana"
text1="orange"
text2="apple"
text3="pear"
if (text!=text1) or (text2!=text3):
    print("None of the values are the same")
else:
    print("At least one value is the same")
n1=int (input("Choose a number"))
n2=int (input("Choose a number"))
n3=int (input("Choose a number"))
n4=int (input("Choose a number"))
if (n1==n2) or (n3==n4):
    print("At least one of the values are the same")
else:
    print("None of the values are the same")

#Write a program to calculate the BMI of a person?
print("BMI Calculator")
weight=float (input("Enter your weight in kilograms"))
height=float (input("Enter your height in meters"))
BMI=weight/(height*height)
print("The BMI is",BMI)
if BMI<=18.4:
    print("You are underweight")
elif BMI<=24.9:
    print("You are healthy")
elif BMI<=34.9:
    print("You are overweight")
else:
    print("You are obese")
print("",BMI)