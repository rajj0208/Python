a = [i*i for i in range(1,11) ]
b = [i*i for i in range(1,11) if i%2]
print(a,b,sep="\n")

l = [4,3,5,6,6,72,46,67,74,2,4,56,77,8,5,42,24,5,66]
# l.sort()

m = [22,33,44,55,56]
l.extend(m)
l.append(0)
print(l)

p = l #same list
q = l.copy() #create a new copy of list


k = l + m  
print(k)

if 54 in l:
    print("Yes 56 is presen in the list")
else:
    print("sorry not present")