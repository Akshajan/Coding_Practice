#mon = (poweri,bonusi)
# n=int(input("enter the num of monsters"))

# defeat n monsters
# monster -> power & bonus 
# player defeat monster  playerpower+=bonus

# n number of monster
# e initial experience
# p b 

n = 5
player_power = 123 #e inintial exp
dungeon = "78 130,10 0,100 343,1000 5,5 500"



def fight(dungeon ,player_power,n):
    count = 0
    # future logic player resurrects not implemented
    monsters = dungeon.split(",")
    sort_monster = []
    for i in monsters:
        sort_monster.append(tuple(i.split(" ")))
    
    
    monsters =  [(int(x), int(y))  for x,y in sort_monster]
    print(monsters)
    monsters.sort(key=lambda x:x[0])
    print(monsters)
    for monst in monsters:
        m_power, m_bonus = monst
        print("<================>")
        print("Starting Fight ->")
        if player_power >= int(m_power):
            player_power+=int(m_bonus)
            print("Hahahaha u r weak. Exp +",m_bonus)     
            count +=1
            
            if count == n:
                print("<================>")
                print("Quest Finished")
                print("Score: ",player_power )
                print("Monsters Slayed: ",count )
                break
            
        else:
            print("You are strong.\nDmn . Im dead")
            print("U r a waste of time")
            print("Score: ",player_power )
            print("Monsters Slayed: ",count )
            break
    return count     

            
fight(dungeon,player_power,n)