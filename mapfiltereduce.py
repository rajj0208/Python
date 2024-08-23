#MAP
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# def cube(x):
#     return x*x*x
# nl = []
# for n in l:
#     nl.append(cube(n))

# print(nl)

nl = list(map(lambda x: x*x*x, l))
print(nl)


#FILTER

nnl = list(filter(lambda x: x%2 == 0, l))
print(nnl)

# REDUCE
from functools import reduce

res = reduce(lambda x, y: x+y, l)
print('Result of reduce is ', res)