# 11. zip(keys, values)
# Zip(keys, values) pairs up items from both lists. dict(zip(...)) converts those pairs into key-value pairs.
keys = ['a', 'b']
values = [1, 2, 3]
print(dict(zip(keys, values))) #Output: {'a’: 1, ‘b’: 2}


# Edge cases :
keys = ['x', 'y', 'z', 'w']
values = [10, 20]
print(dict(zip(keys, values)))  # Output: {'x': 10, 'y': 20}

keys = []
values = [1, 2]
print(dict(zip(keys, values)))  # Output: {}

keys = ['a', 'b']
values = []
print(dict(zip(keys, values)))  # Output: {}

keys = ['a', 'a', 'b']
values = [1, 2, 3]
print(dict(zip(keys, values)))

keys = [['a'], ['b']]
values = [1, 2]
# print(dict(zip(keys, values)))