# problem_24.py
# Filter Long username

usr = ['Laraib', 'Amna', 'Laila','Safdar']

max_len = 4

newUsr = [username for username in usr if len(username) > max_len]

print(newUsr)