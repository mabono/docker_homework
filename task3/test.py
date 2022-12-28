l = [b'a', b'b', b'c']

keys = [b'a', b'b', b'c']
keys2 = []
for key in keys:
    keys2.append(key.decode('ascii'))

values = l
d = dict(zip(keys, values))

print(keys)
print(keys2)
print(d)
