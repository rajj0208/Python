import time
t = time.strftime("%H")
print(t, type(t))
t = int(t)

if(t >= 0 and t < 12):
    print("Good morning sir")
elif(t >= 12 and t < 16):
    print("Good afternoon sir")
elif(t >= 16 and t < 20):
    print("Good evening sir")
else:
    print("Good night sir")