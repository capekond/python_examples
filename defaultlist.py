import collections
data = collections.defaultdict(list)

for k, v in (('a', 'b'), ('a', 'c'), ('b', 'c')):
    data[k].append(v)
pass