age = int(input("enter your age"))

if not age >= 18:
    raise ValueError("Your are underaged and cannot access the site")

print("Welcome to my website")