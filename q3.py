n = int(input("Enter the number of Monsters:"))
e =123
print("Yor initial Experience lvl is",e)

monsters = []

for i in range(n):
    print("Monster count",i+1)
    a = input(f"Enter Power and bonus {i}: ").strip().split()
    b = list(filter(lambda x: x!="",a))
    power,bonus = b
    monsters.append((int(power),int(bonus)))
    
monsters.sort(key= lambda x:x[0])
# monsters =  [(5, 67),(1000,3), (123, 89), (4, 67)]
print(monsters)
c =0 
for enemy in monsters:
    power, bonus = enemy
    
    if(power <= e):
        e += bonus
        c+=1
        print("Score: ",e )
        print("Monsters Slayed: ",c )
        
        if c == n:
            print("You conquered dungeeon")
            print("Score: ",e )
            print("Total Monsters Slayed: ",c )
            break

    else:
        print("dead")
        break
