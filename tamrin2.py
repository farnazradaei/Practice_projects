word = input()  

for i in range(len(word)): 
    for j in range(i + 1):  
        print(word[i], end="")
    for k in range(i + 1, len(word)): 
        print(word[k], end="")
    print() 