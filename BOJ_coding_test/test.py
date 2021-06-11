d1 = dict(zip(['a','b','c'], [1,2,3]))
d2 = dict(zip(['c','b','a'], [3,2,1]))

print(d1 == d2) # True

from collections import OrderedDict
d1 = OrderedDict(a=1, b=2, c=3)
d2 = OrderedDict(c=3, b=2, a=1)

print(d1 == d2) # False