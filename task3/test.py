# l = [b'a', b'b', b'c']

# keys = [b'a', b'b', b'c']
# keys2 = []
# for key in keys:
#     keys2.append(key.decode('ascii'))

# values = l
# d = dict(zip(keys, values))

# print(keys)
# print(keys2)
# print(d)


keys = [b'a', b'b', b'c']
values = [b'1', b'2', b'3']
res = zip(keys, values)
s = ""
for x in res:
    s += f"{x[0].decode('ascii')}: {x[1].decode('ascii')} \n"
print(s)