x = int(input())
aval_hast = True

for i in range(2, x):
    if x % i == 0:
        aval_hast = False
        break

if x > 1 and aval_hast:
    print(x)

else:
    i = 2
    while i <= x:
        if x % i == 0:
            print(i)
            x = x // i  
        else:
            i += 1  



          
        
        
        


    