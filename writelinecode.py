f = open('textfile2.txt', 'w')
l = ['This is line one\n', 'This is line two\n', 'This is line three\n']
f.writelines(l)
f.close()