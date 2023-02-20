
print("replace".center(40, "-"))
st1 = "hello world"
print(f"st1  :{st1}")

res1 = st1.replace("h", "H")
print(f"res1 :{res1}")

res1 = st1.replace("l", "L",2)
print(f"res1 :{res1}")

res1 = st1.replace("l", "L",1)
print(f"res1 :{res1}")

print("-" * 40)
st1 = "the quick brown fox jumps over the lazy dog"
print(f"st1 :{st1}")

res2 = st1.replace("brown fox", "white tiger")
print(f"res2 :{res2}")

res2 = st1.replace("the", "The")
print(f"res2 :{res2}")

res2 = st1.replace("the", "The", 1)
print(f"res2 :{res2}")

print("-" * 40)
# maketrans, translate
st = "hello world"
print(f"st :{st}")

#convert this hello world to HELLO WORLD

a = 'helowrd'
b = 'HELOWRD'
# the length of a and b should be the same

resTbl = st.maketrans(a, b)
print(f"resTbl :{resTbl}")

print("translate".center(40, "-"))
res = st.translate(resTbl)
print(f"res :{res}")
