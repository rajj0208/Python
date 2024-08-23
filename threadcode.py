import threading
import time

def func(sec):
    print(f"Sleeping for {sec} seconds")
    time.sleep(sec)

#normal code
time1 = time.perf_counter()
func(4)
func(2)
func(1)
time2 = time.perf_counter()

print("Normal code is taking time", time2 - time1)

# using thread
time1 = time.perf_counter()
t1 = threading.Thread(target=func, args=[4])
t2 = threading.Thread(target=func, args=[2])
t3 = threading.Thread(target=func, args=[1])

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

time2 = time.perf_counter()
print("Multithread is taking time", time2 - time1)

