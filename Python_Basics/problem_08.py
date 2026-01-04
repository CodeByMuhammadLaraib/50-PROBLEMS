# problem_08.py
# Simple Calculator

def add(a,b):
    return a+b

def subract(a,b):
    return a - b

def multiple(a,b):
    return a*b

def divide(a,b):
    return a/b

def modulus(a,b):
    return a%b

num1 = int(input("Enter 1st num:"))
num2 = int(input("Enter 2nd num:"))

Choice = int(input("Want to>>>\n1. Addition\n2. Subraction\n3. Multiplication\n4. Division\n5. Modulus\n Enter Choice in num:"))

if Choice ==1 :
    print(add(num1,num2))
elif Choice == 2:
    print(subract(num1,num2))
elif Choice == 3:
    print(multiple(num1,num2))
elif Choice == 4:
    print(divide(num1, num2))
elif Choice == 5:
    print(modulus(num1,num2))
else:
    print("Invalid Choice")