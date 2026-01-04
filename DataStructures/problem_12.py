# problem_12.py
# frequency Counter (Word Count)

from collections import Counter

string = "apple mango orange apple banana banana mango grapes orange grapes"
newStirng = string.split()
frequency = Counter(newStirng)

for word, Count in frequency.items():
    print(f"{word} : {Count}")