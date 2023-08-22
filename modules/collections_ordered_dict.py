import collections

print('Ordered dict:')
d = collections.OrderedDict()
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

for k,v in d.items():
    print(k,' -> ',v)


print('Normal dict:')
d = {}
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

for k,v in d.items():
    print(k,' -> ',v)