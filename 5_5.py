#порахувати з допомогою ф-ції скільки разів зустрічається кожен символ в рядку (for couner dict
from collections import Counter
def func(s = ''):
 #   return Counter(s)
    d = {}
    for i in s:
        if i in d.keys():
            d[i] += 1
        else:d[i] = 1
    return d


s = "Hello"
print(func(s))