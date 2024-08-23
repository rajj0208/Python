import string
import random
s = input("Enter your message ")
coding = int(input("Enter 1 for coding and 0 for encoding "))
words = s.split(" ")
if coding:
    wordList = []
    for word in words:
        if(len(word) >= 3):
            r1 = ''.join(random.choices(string.ascii_lowercase, k = 3))
            r2 = ''.join(random.choices(string.ascii_letters, k = 3))
            newWord = word[2:] + word[0:2]
            newWord = r1 + newWord + r2
            wordList.append(newWord)
        else:
            newWord = word[::-1]
            wordList.append(word)
    print(' '.join(wordList)) 
else:
    wordList = []
    for word in words:
        if(len(word) >= 3):
            newWord = word[3:-3]
            nword = newWord[-2:] + newWord[:-2]
            wordList.append(nword)
        else:
            newWord = word[::-1]
            wordList.append(word)
    print(' '.join(wordList))


            