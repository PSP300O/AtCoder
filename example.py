import itertools
a = [(1, 2), (3, 4), (5, 6)]
for p in itertools.product(*a):
    print(p)