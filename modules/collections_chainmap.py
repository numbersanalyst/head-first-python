import collections

a = {'a': 'A', 'b': 'B', 'c': 'C'}
b = {'c': 'c', 'd': 'd', 'e': 'e'}

m = collections.ChainMap(a, b)

print('Values:')
print('a = {}'.format(m['a']))
print('b = {}'.format(m['b']))
print('c = {}'.format(m['c']))
print('d = {}'.format(m['d']))
print('e = {}'.format(m['e']))
print()

print('Keys = {}'.format(list(m.keys())))
print('Values = {}'.format(list(m.values())))
print()

print('Items:')
for k,v in m.items():
    print('{} -> {}'.format(k, v))