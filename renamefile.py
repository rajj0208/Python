import os

files = os.listdir("Desktop/100days")
i = 0
for file in files:
    if file.endswith(".py"):
        os.rename(f"Desktop/100days/{file}", f"Desktop/100days/{i}-Day")
        i += 1