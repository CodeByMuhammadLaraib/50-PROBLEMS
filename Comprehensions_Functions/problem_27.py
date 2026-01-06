# problem_27.py
# Password strength Checker


def pwdStrenghtChecker(pwd):
    if len(pwd) <= 7:
        print("WEAK")

    elif len(pwd) <= 14:
        print("AVERAGE")

    elif len(pwd) <= 21:
        print("STRONG")

    elif len(pwd) <= 28:
        print("very strong")
        
    else:
        print("Super Strong")




pwd = input("Enter Your Password: ")
pwdStrenghtChecker(pwd)

