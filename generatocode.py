#below code explain the usage of generator in python
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b

gen = fibonacci_generator()

for i in range(1, 11):
    print(f"The {i}th fibonacci numebr is", next(gen))