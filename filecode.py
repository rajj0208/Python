#write a file or create
# f = open('myfile.txt', 'w')
# f.write("Hello this is my file")
# f.close

# # read a file

# f = open('myfile.txt', 'r')
# text = f.read()
# print(text)

## append file

# f = open('myfile.txt', 'a')
# f.write("this is appended information")
# f.close()

# without using fclose 

with open('myfile.txt', 'a') as f:
    f.write('i am inside with and i dont have to close the file')

