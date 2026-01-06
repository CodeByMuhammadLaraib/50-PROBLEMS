# problem_22.py
# Even numbers using Comprehension

Lis = []
Num = 2
ran = int(input("Enter a Range: "))
newLis = [Num for Num in range(ran + 1) if Num % 2 == 0]

print(newLis) 