# problem_23.py
# Dictionary comprehension (id → square)

Dic = {}

Num = int(input("Enter the Number: "))
ran = int(input("Enter range: "))

newDic = {Num : Num*Num for Num in range(ran)}

print(newDic)