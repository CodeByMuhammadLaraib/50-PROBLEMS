# problem_29.py
# Flatten nested list

nested_list = [[1,2,3], [4,5,6], [7,8,9]]

flatten_list = [i for fl in nested_list for i in fl]
print(flatten_list)