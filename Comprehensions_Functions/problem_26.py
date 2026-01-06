# problem_26.py
# Function Calculator

def Addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def Multiplication(a, b):
    return a * b


def Division(a, b):
    return a / b


def Modulus(a, b):
    return a % b



a = int(input("Enter Number: "))
b = int(input("Enter Number: "))

choice = input(
    "\nChoose an Option;\n"
    "1: Add\n"
    "2: subract\n"
    "3: Multiply\n"
    "4: Divide\n"
    "5: Modulus\n"
    "\nChoose: "
)

if choice == '1':
   result = Addition(a, b)
   print(result)

elif choice == '2':
    result = subtraction(a, b)
    print(result)

elif choice == '3':
    result = Multiplication(a, b)
    print(result)

elif choice == '4':
    result = Division(a, b)
    print(result)

elif choice == '5':
    result = Modulus(a, b)
    print(result)

else:
    print("INVALID CHOICE")

