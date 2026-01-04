# problem_07.py
# Palindrome check

def is_palindrome_string(s):
    return s == s[::-1]

# Example usage
input_string = input("Enter a string: ")
if is_palindrome_string(input_string):
    print("The string is a palindrome.")
else:
    print("Not a palindrome.")
