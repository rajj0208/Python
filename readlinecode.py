f = open('textfile.txt', 'r')
while True:
    lines = f.readline()
    if not lines:
        break
    m1 = lines.split(',')[0]
    m2 = lines.split(',')[1]
    m3 = lines.split(',')[2]

    print(f'Makrs of student id 100\n English: {m1}, Math: {m2}, SST: {m3}')
f.close()

