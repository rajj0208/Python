def pack1():
    print("this is my package")

s = "This is my own package"

print(__name__)


# we want to import this "raj" file and donnot want that script to execute just by 
# importing the file, if we will import raj then the value of __name__ will be 
# changes to "raj" 
if __name__ == "__main__":
    pack1()