# try:
#     l = [3,4,5,6,7,7,8]
#     n = int(input("enter the number"))
#     print("the value at nth index", l[n])
# except:
#     print("Invalid Input")
# # finally:
# #     print("I will always execute")
# print("I will always execute")

def fun1():
    try:
        l = [3,4,5,6,7,7,8]
        n = int(input("enter the number"))
        print("the value at nth index", l[n])
        return 1
    except:
        print("Invalid Input")
        return 0
    finally:
        print("I will always execute")

x = fun1()
print(x)