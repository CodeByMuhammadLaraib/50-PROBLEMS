# problem_17.py
# Menu driven list program


def display_menu():
    print("\nMenu:")
    print("1. Add an item to the list")
    print("2. Remove an item from the list")
    print("3. Display the list")
    print("4. Exit")

def main():
    my_list = []

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            item = input("Enter the item to add: ")
            my_list.append(item)
            print(f"'{item}' has been added to the list.")

        elif choice == '2':
            item = input("Enter the item to remove: ")
            try:
                my_list.remove(item)
                print(f"'{item}' has been removed from the list.")
            except ValueError:
                print(f"'{item}' is not in the list.")

        elif choice == '3':
            print("Current list:", my_list)

        elif choice == '4':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
