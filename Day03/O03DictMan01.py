
d1 = dict()
print(f"d1 :{d1}")
print(type(d1))

print("-" * 40)
d2 = {'name': 'Robert', 'age': 30, 'desig': 'BDM', 'dept': 'MKT', 'sal': 45000}
print(f"d2 :{d2}")
print(type(d2))

print("-" * 40)
d3 = dict([('name', 'sachin'),('age', 32), ('runs', 130), ('oppn', 'Aus')])
print(f"d3 :{d3}")
print(type(d3))

print("-" * 40)
d4 = dict(name='Tina', age=8, cls='3rd D', school="NPS")
print(f"d4 :{d4}")
print(type(d4))

print("-" * 40)
# create
player = {'name': 'Sachin', 'age': 32, 'runs': 85, 'oppn': 'Aus'}
print(f"player :{player}")

print("-" * 40)
# read
print(f"Name :{player['name']}")
print(f"runs :{player['runs']}")

print("-" * 40)
# iterate
for x in player:
    print(x, "=>", player[x])                    # pointing to the keys

print("-" * 40)
# modify

print(f"player :{player}")
player['name'] = "Sachin Tendulkar"
player['runs'] = 105
player['venue'] = 'Perth'

print(f"player :{player}")

print("-" * 40)
# delete

del player['age']
del player['venue']

print(f"player :{player}")

print("-" * 40)
print(dir(d1))



