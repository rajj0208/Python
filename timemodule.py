import time

# def useFor():
#     i = 0
#     for i in range(10000000):
#         i = i+1

# start = time.time()
# useFor()
# print(time.time() - start)

print("I will wait for 5 seconds")
time.sleep(5)
print("Thanks for waiting")

t = time.localtime()

mytime = time.strftime("%Y/%m/%d %H:%M:%S", t)
print(mytime)
