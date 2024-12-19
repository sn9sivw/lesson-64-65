from collections import Counter
from random import randint

print("Массив:")
a = [randint(0, 10) for i in range(10)]
print(a)

print("После сортировки:")
a = sorted(a)
c = Counter(a)
print(a)
print(c)
