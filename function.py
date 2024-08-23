def cal_avg(a ,b, c):
    print("the average of the numbers are", (a+b+c)/3)

cal_avg(3,6,9)

#default values

def avg(a, b , c = 1):
    print("the average is", (a+b+c)/3)

avg(3,8)

#passing argument with key values

avg(c = 3, b = 1, a= 10)

# variable length argument

def avg3(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum/len(numbers)

ans = avg3(3,4,5,6,7,33,4,6)
print("the average of all the numbers is ", ans)


def fun(**names):
    print("the last name of the person is ", names["lastname"])

fun(fname = "raj", mname = " ", lastname = "Jaiswal")

