d = {"foo": 12, "bar": 17, "qux": 2}

items = list(d.items())

# Sort by key

items.sort()

for i in items:
    print(f'{i[0]: {i[1]}}')

# Sort by value

# def sort_by(t):
#     # print(f'sort_by(repr(t)) called!')
#     return t[1]

# items.sort(key=sort_by)

# for i in items:

items.sort(key=lambda t: t[1])