
l1 = list()
print(f"l1 :{l1}")
print(type(l1))

print("-" * 40)
l2 = [1, 2, 3, 'four', 'five', 'six', 7.0, 8.6, 9.2, 10+2j, 10-2j, True, False]
print(f"l2 :{l2}")
print(type(l2))

print("-" * 40)
l3 = list(range(1, 11))
print(f"l3 :{l3}")
print(type(l3))

print("-" * 40)
# hetrogenous collection
l4 = [1, 2, 3, 'four', 'five', 'six', 7.0, 8.6, 9.2, 10+2j, 10-2j, True, False]
print(f"l4 :{l4}")

print("-" * 40)
# memory allocation is not contigious
print(f"id(l4[0]) :{id(l4[0])}")
print(f"id(l4[1]) :{id(l4[1])}")
print(f"id(l4[2]) :{id(l4[2])}")
print(f"id(l4[3]) :{id(l4[3])}")

print("-" * 40)
# print the elements of list
print(f"l4[1] :{l4[1]}")
print(f"l4[5] :{l4[5]}")

# iterate through a list
for i in l4:
    print(i, end=" ")
print()

print("-" * 40)
# modify the list
l4[2] = 33
l4[8] = 900
# l4[13] = "hello"            # add a new element

print(f"l4 :{l4}")

print("-" * 40)
# delete
del l4[10]
del l4[9]

print(f"l4 :{l4}")

print("-" * 40)
print(dir(l1))