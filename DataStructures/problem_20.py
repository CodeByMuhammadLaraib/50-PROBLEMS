# problem_20.py
# simple login system

user = {
    "admin" : "1234",
}
def login():
    username = input("ENTER USERNAME: ").lower()
    password = input("ENTER PASSWORD: ")

    if username in user and user[username] == password:
        print("Login successful...")

        if username == "admin" and username in user and user[username] == password:
            Choice = input(
                "\n1: Create user\n"
                "2: delete user\n"
                "3: exit\n"
                "Enter Choice: "
                )
            
            if Choice == '1':
                registration()

            elif Choice == '2':
                pop_user()

            elif Choice == '3':
                print("program Exiting...")
                return
            else:
                print("INVALID INPUT")
        
        else:
            print("NOT AN ADMIN")

    else:
        print("incorrect username and password...!")


def registration():
    print("USER CREATING...")

    username = input("username: ")
    password = input("password: ")

    if username in user:
        print("user already exist please try again.")
    
    else:
        user[username] = password
        print("user Add Successful")



def pop_user():
    username = input("username: ")

    if username not in user:
        print("username name is not exist")

    else:
        del user[username]
        print("user is deleted...")


login()