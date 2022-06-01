# changing value out in list
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"
print(fruits)

#subtract one list from another ,removing values that appear in both
def array_diff(a, b):
    return [x for x in a if x not in b]

