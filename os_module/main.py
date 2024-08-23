import os as o

if(not o.path.exists("data")):
    o.mkdir("data")


for i in range(15):
    o.mkdir(f"data/Day-{i}")