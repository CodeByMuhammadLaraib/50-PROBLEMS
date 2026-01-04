# problem_18.py
# Stack using list


# Initialize an empty stack
stack = []

# Function to push an item onto the stack
def push(item):
    stack.append(item)

# Function to pop an item from the stack
def pop():
    if not is_empty():
        return stack.pop()
    else:
        return "Stack is empty"

# Function to peek at the top item of the stack
def peek():
    if not is_empty():
        return stack[-1]
    else:
        return "Stack is empty"

# Function to check if the stack is empty
def is_empty():
    return len(stack) == 0

# Example usage
push(10)
push(20)
push(30)

print(peek())        # Output: 30
print(pop())         # Output: 30
print(pop())         # Output: 20
print(is_empty())    # Output: False
print(pop())         # Output: 10
print(is_empty())    # Output: True
print(pop())         # Output: Stack is empty
