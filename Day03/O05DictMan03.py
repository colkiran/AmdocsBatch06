
print("pop".center(40, "-"))
player = {'name': 'Sachin Tendulkar', 'age': 32, 'runs': 105, 'oppn': 'Aus', 'venue': 'Perth'}

print(f"player :{player}")

res = player.pop('age')
print(f"res :{res}")

res = player.pop('oppn')
print(f"res :{res}")

print(f"player :{player}")

print("popitem".center(40, "-"))

player = {'name': 'Sachin Tendulkar', 'age': 32, 'runs': 105, 'oppn': 'Aus', 'venue': 'Perth'}

print(f"player :{player}")

print("-" * 40)

res = player.popitem()
print(f"res :{res}")

res = player.popitem()
print(f"res :{res}")

print(f"player :{player}")

print("items".center(40, "-"))
# its a combination keys and values

emp = {
    'emp1': {'name': "Mark", 'age': 35, 'desig': 'TL', 'dept': 'finance', 'sal': 75000},
    'emp2': {'name': "Sophia", 'age': 30, 'desig': 'Mkt Exe', 'dept': 'MKT', 'sal': 45000},
    'emp3': {'name': "Stephen", 'age': 37, 'desig': 'PM', 'dept': 'IT', 'sal': 145000}
}

print(f"emp :{emp}")

print("-" * 40)

print(f"emp1 :{emp['emp1']}")
print(f"emp2 :{emp['emp2']}")
print(f"emp3 :{emp['emp3']}")

print("-" * 40)

for ky, info in emp.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k, "=>", v)
    print("-" * 40)

print("update".center(40, "-"))
emp1 =  {'name': "Mark", 'age': 35, 'desig': 'TL', 'dept': 'finance'}
emp2 = {'name': "Sophia", 'age': 30, 'desig': 'Mkt Exe', 'sal': 45000}

print(f"emp1 :{emp1}")
print(f"emp2 :{emp2}")

print("-" * 40)

emp1.update(emp2)
print(f"emp1 :{emp1}")
