name = input().lower()
counts={}

for element in name:
    if element.isalpha():
        if element in counts:
            counts[element]+=1
        else:
            counts[element]=1

unique_count=sum(1 for value in counts.values() if value==1 )
if unique_count % 2 == 1 :
    print("Alien")
else:
    print("Human")
