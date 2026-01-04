# porblem_15.py
# Find common in 2 list

lsi1 = ["Amna", 22, "Haider"]
lis2 = [ "Amna", 21, 33, 34]

"""for i in lsi1:
    #print(i)
    for n in lis2:
        if n == i:
            print(i)
"""
commonWord = [i for i in lsi1 for n in lis2 if n == i]
print(commonWord)