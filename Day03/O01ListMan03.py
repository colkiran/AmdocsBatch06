
print("remove".center(40, "-"))

l1 = [1, 1, 1, 2, 3, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2 ,2, 1, 1, 1, 2, 3, 1, 2, 2, 2, 2, 2, 2, 1, 2, 3, 1, 2, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1, 1, 2 ,2, 2, 2, 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

print(f"l1 :{l1}")

print("-" * 40)

l1.remove(3)
l1.remove(3)
print(l1)

print("-" * 40)

while l1.count(1):
    l1.remove(1)

print(f"l1 :{l1}")

print("index".center(40, "-"))

l1 = [1, 1, 1, 2, 3, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2 ,2, 1, 1, 1, 2, 3, 1, 2, 2, 2, 2, 2, 2, 1, 2, 3, 1, 2, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1, 1, 2 ,2, 2, 2, 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

print(f"l1 :{l1}")

print("-" * 40)
print("3 :", l1.count(3))
print("1st 3 :", l1.index(3))
print("2nd 3 :", l1.index(3, l1.index(3)+1))
print("2nd 3 :", l1.index(3, l1.index(3, l1.index(3)+1)+1))

print("copy".center(40, "-"))
l1 = list(range(1, 6))
print(f"l1 before :{l1}")

l2 = l1         # shallow copy - copies the data along with the address

print(f"l2 before :{l2}")
l2.append(6)
l2.append(7)
l2.append(8)

print("-" * 40)
print(f"l2 after :{l2}")
print(f"l1 after :{l1}")

print("\n", "-" * 40,  "\n")

l3 = [2, 4, 6, 8, 10]
print(f"l3 before :{l3}")

l4 = l3.copy()

print(f"l4 before:{l4}")

l4.extend([12, 14, 16, 18])

print("-" * 40)
print(f"l4 after :{l4}")
print(f"l3 after :{l3}")

print("\n", "-" * 40,  "\n")

l5 = [1, 2, 3, [10, 20, 30, 40, 50], 4, 5]
print(f"l5 before :{l5}")

l6 = l5.copy()

print(f"l6 before :{l6}")
l6[3].append(60)
l6[3].append(70)
l6[3].append(80)

print("-" * 40)
print(f"l6 after :{l6}")
print(f"l5 after :{l5}")

print("\n", "-" * 40,  "\n")
l7 = [1, 2, 3, 4, [5, 10, 15, 20, 25], 5]
print(f"l7 :{l7}")
from copy import deepcopy

l8 = deepcopy(l7)

l8[4].extend([30, 35, 40, 45])
print("-" * 40)

print(f"l8 after :{l8}")
print(f"l7 after :{l7}")
