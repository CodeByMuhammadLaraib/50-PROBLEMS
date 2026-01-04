# problem_14.py
# Merge two Dictionary

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged_dict = {key:value  for d in (dict1, dict2) for key, value in d.items()}
print(merged_dict)
