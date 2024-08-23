def fun(x):
    return x*2

lfun = lambda x: x*2

print(fun(5))
print(lfun(6))

fun2 = lambda x, y: print(f"{x} * {y} = {x*y}")

fun2(9, 6)

# lambda function are generally used for passing small fucntions as an argument

def fun3(fx):
    return 10 + fx(10)

print(fun3(lfun))   