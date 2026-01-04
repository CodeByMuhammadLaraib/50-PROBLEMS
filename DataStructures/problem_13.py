# problem_13.py
# Sort Dictionary values

from operator import itemgetter
Dic = {
    "Amar" : 32,
    "Iqra" : 17,
    "Qanwal" : 18
}
newDic = dict(sorted(Dic.items(), key = itemgetter(1)))
print(newDic)