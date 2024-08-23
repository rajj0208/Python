marks = [34,76,95,23,11,34,56,64,77]

# i = 0
# for m in marks:
#     print(m)
#     if(i== 2):
#         print("Highest makrs!!")
#     i += 1

#To solve the above problem use enumerate

for i, m in enumerate(marks):
    print(m)
    if(i == 3):
        print("Highest marks!!")
