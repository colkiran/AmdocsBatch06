
st = "hello world"
print(f"st :{st}")
print(type(st))

print("-" * 40)
# strings are immutable
# print(f"st[0] :{st[0]}")           # strings are stored like list(array)
# st[0] = "H"                     # strings are immutable
# we dont have a setter method

print(f"st[0] :{st[0]}")
print(f"st[6] :{st[6]}")
print(f"st[10] :{st[10]}")

print("-" * 40)
# slicing
print(f"st[0:5]  :{st[0:5]}")
print(f"st[6:11] :{st[6:11]}")
print(f"st[0:11] :{st[0:11]}")
print(f"st[0:]   :{st[0:]}")
print(f"st[:11]  :{st[:11]}")
print(f"st[:]    :{st[:]}")

print("-" * 40)
# reverse indexes
print(f"st[-1]  :{st[-1]}")
print(f"st[-7]  :{st[-7]}")
print(f"st[-11] :{st[-11]}")

print("-" * 40)
# slicing
print(f"st[-1: -6: -1]  :{st[-1: -6: -1]}")
print(f"st[-7: -12: -1] :{st[-7: -12: -1]}")
print(f"st[-1: -12: -1] :{st[-1: -12: -1]}")
print(f"st[-1: :-1]     :{st[-1: :-1]}")
print(f"st[ : -12: -1]  :{st[ :-12: -1]}")
print(f"st[::-1]        :{st[::-1]}")


print("-" * 40)
# use indexing and find if the given string is a palindrome
st = "malayalam"
print(f"Palindrome {st}" if st == st[::-1] else f"Not a Palindrome {st}")

# print("-" * 40)
# print(dir(st))
# 40 - 5 = 35 // 2 = 17
print("find".center(40, "-"))

st1 = "hello world"
st2 = "the quick brown fox jumps over the lazy dog"

print(f"st1 :{st1}")
res = st1.find("w")
print(f"res :{res}")

res1 = st1.find("l")
print(f"res1 :{res1}")

res1 = st1.find("l", st1.find("l")+1)
print(f"res1 :{res1}")

res1 = st1.find("l", st1.find("l", st1.find("l")+1)+1)
print(f"res1 :{res1}")

print("-" * 40)

print(f"st2 :{st2}")
print(f"st2.find('fox')     :{st2.find('fox')}")
print(f"1st st2.find('the') :{st2.find('the')}")
print(f"2nd st2.find('the') :{st2.find('the', st2.find('the')+1)}")


