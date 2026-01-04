# problem_19.py
# Queue using list

queue = []


def enqueue(item):
    queue.append(item)
    print(f"{item} added to queue")


def dequeue():
    if is_empty():
        print("Queue is empty")
    else:
        item = queue.pop(0)
        print(f"{item} removed from queue")


def peek():
    if is_empty():
        print("Queue is empty")
    else:
        print(f"{queue[0]} is the first element")


def is_empty():
    return len(queue) == 0


def size():
    print(f"Queue size: {len(queue)}")


def starter():
    while True:
        choice = input(
            "\nChoose Option\n"
            "1: Enqueue\n"
            "2: Dequeue\n"
            "3: Peek\n"
            "4: Size\n"
            "5: Exit\n"
            "Enter choice: "
        )

        if choice == "1":
            item = input("Enter item: ")
            enqueue(item)

        elif choice == "2":
            dequeue()

        elif choice == "3":
            peek()

        elif choice == "4":
            size()

        elif choice == "5":
            print("Program exiting...")
            break

        else:
            print("INVALID INPUT")


if __name__ == "__main__":
    starter()
