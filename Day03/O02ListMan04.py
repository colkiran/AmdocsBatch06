
"""
sort        -   sort the original list
sorted      -   creates a copy of the list then sorts and returns it

"""

print("sort".center(40, "-"))

l1 = [9, 5, 8, 1, 10, 2, 4, 6, 3, 7]
print(f"l1 :{l1}")

res_asc = sorted(l1)
print(f"ascending: {res_asc}")

res_desc = sorted(l1, reverse=True)
print(f"descending :{res_desc}")

print("-" * 40)

l1 = [9,'zebra', 5, 'apple', 8, 'yellow', 1,  'blue', 10, 'white', 2, 'green', 4, 'red',  6, 'violet', 3, 'maroon', 7, 'cat', 'dog', 'pink', 198, 1502, 12345, 29, 282, 2503, 2198]

print(f"l1 :{l1}")

print("-" * 40)

res = sorted(l1, key=ascii)
print(res)

print("-" * 40)

print(res.index(1))
print(len(res)-1)

l2 = res[12:29]
l2.sort()

res1 = res[0:12] + l2

print(res1)

print("-" * 40)

cities = ['newyork', 'delhi', 'philadelphia', 'muscat', 'hyderabad', 'manali',
          'california', 'dublin', 'perth', 'melbourne']

print(f"cities :{cities}")

# sort the cities based on their length
print("-" * 40)
res = sorted(cities, key=len)
print(f"res :{res}")

print("-" * 40)

months = ['dec', 'sep', 'aug',  'nov', 'feb', 'apr', 'jan', 'mar', 'jun', 'may', 'jul', 'oct']

print(months)

# sort these months

print("-" * 40)

from calendar import month_abbr
month_list = []

for mth in list(month_abbr):
    month_list.append(mth.lower())

res = sorted(months,key=month_list.index)
print(res)

print("-" * 40)

my_dict = {'jan': 1, 'feb':2, 'mar':3, 'apr':4, 'may':5, 'jun':6, 'jul':7 , 'aug':8, 'sep':9, 'oct':10, 'nov':11, 'dec':12}

print(sorted(months, key=my_dict.get))

print("reversed".center(40, "-"))

l1 = [9, 5, 8, 1, 10, 2, 4, 6, 3, 7]
print(f"l1 :{l1}")

print("-" * 40)

print(list(reversed(l1)))
