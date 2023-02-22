

print("keys".center(40, "-"))

player = {'name': 'Sachin Tendulkar', 'age': 32, 'runs': 105, 'oppn': 'Aus', 'venue': 'Perth'}

print(f"player :{player}")

print("-" * 40)
k = player.keys()
print(F"k :{k}")

print("-" * 40)
for k in player.keys():
    print(k, "=>", player[k])

print("values".center(40, "-"))

player = {'name': 'Sachin Tendulkar', 'age': 32, 'runs': 105, 'oppn': 'Aus', 'venue': 'Perth'}

print(f"player :{player}")

v = player.values()
print(f"v :{v}")

print("get".center(40, "-"))

player = {'name': 'Sachin Tendulkar', 'age': 32, 'runs': 105, 'oppn': 'Aus'}

print(f"player :{player}")

print("-" * 40)
print(player.get('name', "Invalid key, Please enter a valid key"))
print(player.get('venue', "Invalid key, Please enter a valid key"))

print("fromkeys".center(40, "-"))
cities = ['del', 'lon', 'nyk', 'tky', 'tor', 'prt']
print(f"cities :{cities}")

print("-" * 40)
# convert the list into a dictionary and list elements should become keys

res1 = dict.fromkeys(cities)
print(f"res1 :{res1}")

res2 = dict.fromkeys(cities, 24)
print(f"res2 :{res2}")

print("setdefault".center(40, "-"))
player = {'name': 'Sachin Tendulkar', 'age': 32, 'runs': 105, 'oppn': 'Aus'}
print(f"player :{player}")

print("-" * 40)
player.setdefault("name", "sachin")
player.setdefault("age", 30)
player.setdefault('venue', "MCG")

print(f"player :{player}")
