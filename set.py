s = {1,2,3,4,5,5,6,7,7,8,8,9}
print(type(s))
print(s)

s2 = {8, 9 , 10, 11, 12, 13, 14}

# print(s.union(s2))
# print(s, s2)
# s.update(s2)
# print(s.intersection(s2))
# s.intersection_update(s2)
# for x in s2:
#     print(x)
# print(11 in s)

# print(s.symmetric_difference(s2))
# print(s.symmetric_difference_update(s2))
print(s.difference(s2))
s.discard(44)
s.add(62)

print(s)
