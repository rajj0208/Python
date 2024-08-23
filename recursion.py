def fact(n):
    if(n == 0 or n == 1):
        return 1
    return fact(n-1)*n

num = int(input("enter the number"))
res = fact(num)

print("The factorial of the number", num, "is", res)

def fib(n):
    if(n==0):
        return 0
    if(n==1):
        return 1
    return fib(n-1) + fib(n-2)
print("The nth fibonacci number is ", fib(num))