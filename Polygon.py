import sys
import iri

# iri.launch()

list_1 = [5, 4, 3, 2, 1]
list_2 = ['a', 'l', 'i', 'r', 'i']

list_1, list_2 = zip(*sorted(zip(list_2, list_1)))
print(list_1)
print(list_2)

if isinstance('', list):
    print("Hey")
else:
    print("Hoy")
