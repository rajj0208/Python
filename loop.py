color = ["red", "blue", "green", "black"]

for c in color:
    print(c)
    for n in c:
        print(n)

for n in range(1, 10, 2):
    print(n)

count = 5
while(count > 0):
    print(count)
    count = count - 2
else:
    print("out of the loop value is", count)