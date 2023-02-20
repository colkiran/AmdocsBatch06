
print("format".center(40, "-"))

# emulate c style
str = "Welcome %s, what a %s player"
print(f"str :{str}")

values = ("Sachin", "superb")           # tuple
print(values)

print("-" * 40)
print(str, values)
print(str % values)

print("-" * 40)
print("Welcome %s, with a rating of %d what a %s player" %  ("Sachin", 4, "class"))
print("Welcome %s, with a rating of %d what a %s player" %  ("Sachin", 4.72323453, "class"))
print("Welcome %s, with a rating of %.3f what a %s player" %  ("Sachin", 4.72323453, "class"))

print("-" * 40)
# interpolation - f string
from math import pi, e

print(f"PI = {pi} and euler's constant :{e}")
print(f"PI = {pi:.3f} and euler's constant :{e:.3f}")
sname = "Sachin"
rating = 4.866954
adj = "class"
print(f"Welcome {sname}, with a rating of {rating:.3f} what a {adj} player")

# format of string class
print("Welcome {}, what a {} player".format("Sachin", "class"))
print("Welcome {0}, what a {1} player".format("Sachin", "class"))
print("Welcome {0}, what a {1} player for {2}".format("Sachin", "class", "India"))
print("Welcome {2}, what a {0} player for {1}".format("Sachin", "class", "India"))
print("Welcome {gname}, what a {adj} player for {ctr}".format(gname="Sachin", adj="class", ctr="India"))

print("Welcome {}, what a {} player for {ctr}".format("Sachin", "class", ctr="India"))
print("Welcome {}, with a rating of {rating} what a {adj} player for {ctr}".format("Sachin", rating=4, adj="class", ctr="India"))

print("Welcome {}, with a rating of {rating:.3f} what a {adj} player for {ctr}".format("Sachin", rating=4.8923443, adj="class", ctr="India"))

print("Welcome {0}, with a rating of {1:.3f} what a {2} player for {3}".format("Sachin", 4.8923443, "class", "India"))

print("-" * 40)
print("{} {}".format("Sachin","Tendulkar"))
print("{fn} {ln}".format(fn="Sachin",ln="Tendulkar"))
# reserve's 15 spaces for fn
print("{fn:15}{ln}".format(fn="Sachin",ln="Tendulkar"))
print("{fn:15}{ln}".format(fn=100,ln="Tendulkar"))
print("{fn:5} {ln}".format(fn=100,ln="Tendulkar"))
print("{fn} {ln}".format(fn=3435569833,ln="Tendulkar"))

print("-" * 40)
pname = "Sachin Tendulkar"
print("{pname}".format(pname="Sachin Tendulkar"))
print("{pname:.6}".format(pname="Sachin Tendulkar"))

print("-" * 40)
print("{fn:>15} {ln}".format(fn = "Sachin", ln = "Tendulkar"))
print("{fn:^15} {ln}".format(fn = "Sachin", ln = "Tendulkar"))
print("{fn:<15} {ln}".format(fn = "Sachin", ln = "Tendulkar"))

print("-" * 40)
print("{fn:->15} {ln}".format(fn = "Sachin", ln = "Tendulkar"))
print("{fn:*^15} {ln}".format(fn = "Sachin", ln = "Tendulkar"))
print("{fn:#<15} {ln}".format(fn = "Sachin", ln = "Tendulkar"))

print("-" * 40)
print("{num:5}".format(num=23))
print("{num:05}".format(num=23))

