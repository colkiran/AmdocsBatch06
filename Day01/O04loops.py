
# for loop - foreach loop it depends on a collection
# while

"""
print(data, sep="", end="\n")
for loop -> continue, break, else
"""

for i in range(1, 11):
    print(i, end=" ")
print()

for i in range(1, 26):
    # if i > 20:
    #     break
    if i % 2 == 1:
        continue
    print(i, end=" ")
else:
    print("\n Iterations completed......")

print("-" * 40)

x = 1
while x <= 10:
    print(x, end=" ")
    x += 1
print()

print("-" * 40)

for i in range(10, 0, -1):
    print(i, end=" ")
print()