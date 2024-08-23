# try:
#     num = int(input("enter the number:"))
#     for i in range(1, 11):
#         print(f"Value of {num}*{i} is {num*i}")
# except Exception as e:
#     print("Invalid input")
#     print(e)


try:
    num = int(input("Enter the number"))
    l = [3,4,5,6]
    print(l[num])
except ValueError:
    print("Invalid Input")
except IndexError:
    print("out of bound excess")

print("some important line of code you want to execute irrespective of error")