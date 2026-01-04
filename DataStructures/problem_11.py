# problem_11.py
# remove Duplicates from list

lis = [21, "emma", 21, 594, "emma", "sallu", 33, 41]

newLis = []

[newLis.append(x) for x in lis if x not in newLis]

print(newLis)