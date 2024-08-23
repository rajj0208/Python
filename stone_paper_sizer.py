import random
def check(comp, user):
    if(comp == user):
        return 0
    if(comp == 0 and user == 1):
        return 1
    if(comp == 1 and user == 2):
        return 1
    if(comp == 2 and user == 0):
        return 1
    return -1
d = {0 : "Stone", 1 : "Paper", 2 : "Sizer"}
count = 0
userCount = 0
compCount = 0
while(count < 3):
    comp = random.randint(0, 2)
    user = int(input("Choose 0 for stone, 1 for Paper and 2 for Sizer "))

    print(f"You have chosen : {d[user]}")
    print(f"Computer have chosen: {d[comp]}")

    result = check(comp, user)
    if(result == 0):
        print("Draw")
        continue
    elif(result == 1):
        print("You Won")
        userCount = userCount + 1
    else:
        print("You Lost")
        compCount = compCount + 1
    count = count+1

if userCount > compCount:
    print("Finally User won the Match")
else:
    print("Finally Computer won the Match")

