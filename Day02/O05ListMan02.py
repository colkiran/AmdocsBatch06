
# add new values into the list - append, extend, insert

print("append".center(40, "-"))
l1 = list(range(2, 11, 2))
print(f"l1 :{l1}")
print(type(l1))

l1.append(12)
l1.append(14)
l1.append(16)
print(f"l1 :{l1}")

l1.append([18, 20, 22, 24, 26])
print(f"l1 :{l1}")
print(l1[8][1:4])

print("extend".center(40, "-"))
l2 = list(range(1, 11))
print(f"l2 :{l2}")

l2.extend([11, 12, 13])
l2.extend([15, 16, 17])

print(f"l2 :{l2}")

print("insert".center(40, "-"))
l3 = list(range(1, 6))
print(f"l3 :{l3}")

l3.insert(1, 1.5)
l3.insert(3, 2.5)
l3.insert(5, 3.5)
l3.insert(7, 4.5)

print(f"l3 :{l3}")

l3.insert(15, 5.5)
print(f"l3 :{l3}")

print("-" * 40)
# delete values from a list - pop, remove, clear

print("count".center(40, "-"))

l1 = [1, 1, 1, 2, 3, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2 ,2, 1, 1, 1, 2, 3, 1, 2, 2, 2, 2, 2, 2, 1, 2, 3, 1, 2, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1, 1, 2 ,2, 2, 2, 1]

print(f"l1 :{l1}")

print(f"1 :{l1.count(1)}")
print(f"2 :{l1.count(2)}")
print(f"3 :{l1.count(3)}")
print(f"9 :{l1.count(9)}")

print("pop".center(40, "-"))
l2 = list(range(1, 11))
print(f"l2 :{l2}")

res = l2.pop(7)
print(res)

res = l2.pop(3)
print(res)

res = l2.pop()
print(res)

res = l2.pop()
print(res)

print(f"l2 :{l2}")

print("clear".center(40, "-"))
l3 = list(range(1, 6))
print(f"l3 :{l3}")

l3.clear()
print(f"l3 :{l3}")

