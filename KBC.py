question = [["Who is the prime minister of India", "Narendra Modi", "Rahul Gandhi", "Arvind Kejriwal", "Yogi", "1"],
            ["Who is the prime minister of India", "Narendra Modi", "Rahul Gandhi", "Arvind Kejriwal", "Yogi", "1"],
            ["Who is the prime minister of India", "Narendra Modi", "Rahul Gandhi", "Arvind Kejriwal", "Yogi", "1"],
            ["Who is the prime minister of India", "Narendra Modi", "Rahul Gandhi", "Arvind Kejriwal", "Yogi", "1"],
            ["Who is the prime minister of India", "Narendra Modi", "Rahul Gandhi", "Arvind Kejriwal", "Yogi", "1"],
            ["Who is the prime minister of India", "Narendra Modi", "Rahul Gandhi", "Arvind Kejriwal", "Yogi", "1"],
            ["Who is the prime minister of India", "Narendra Modi", "Rahul Gandhi", "Arvind Kejriwal", "Yogi", "1"],
            ["Who is the prime minister of India", "Narendra Modi", "Rahul Gandhi", "Arvind Kejriwal", "Yogi", "1"],
            ["Who is the prime minister of India", "Narendra Modi", "Rahul Gandhi", "Arvind Kejriwal", "Yogi", "1"],
            ["Who is the prime minister of India", "Narendra Modi", "Rahul Gandhi", "Arvind Kejriwal", "Yogi", "1"],
            ["Who is the prime minister of India", "Narendra Modi", "Rahul Gandhi", "Arvind Kejriwal", "Yogi", "1"],
            ["Who is the prime minister of India", "Narendra Modi", "Rahul Gandhi", "Arvind Kejriwal", "Yogi", "1"],
            ["Who is the prime minister of India", "Narendra Modi", "Rahul Gandhi", "Arvind Kejriwal", "Yogi", "1"],
            ["Who is the prime minister of India", "Narendra Modi", "Rahul Gandhi", "Arvind Kejriwal", "Yogi", "1"],
            ]

level = [1000, 2000, 3000, 5000, 10000, 20000, 50000, 100000, 200000, 500000,
         1000000, 2000000, 5000000, 10000000]

money = 0
for i in range(len(question)):
    ques = question[i]
    print(ques[0])
    print(f"1. {ques[1]}           2. {ques[2]}\n3. {ques[3]}           4. {ques[4]}")
    ans = input("Enter your answer or enter 0 to quit: ")
    if(ans == "0"):
        money = level[i-1]
        break
    if(ans == ques[5]):
        print("Congratulation! Correct answer")
    else:
        print("Wrong answer")
        break
    if(i == 3):
        money = 5000
    elif(i == 5):
        money = 20000
    elif(i == 7):
        money = 100000
    elif(i== 9):
        money = 500000
    
print(f"You have won {money} rupees")


            