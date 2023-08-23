import collections

c = collections.Counter()
print('init:', c)

c.update('cdfeffdccccc')
print('sequence:', c)

c.update({'a': 102, 'b': 2})
print('dict:', c)
