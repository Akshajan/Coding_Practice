n = int(input("Enter the number of Monsters:"))
e =123
print("Yor initial Experience lvl is",e)
l=[]
b=[]
for i in range(n):
    print("Monster count",i+1)
    l.append(int(input("Enter the Power :")))
    b.append(int(input("Enter the bonus :")))
for i in range(n):
    for j in range(n-1):
        if l[j]>l[j+1]:
            temp = l[j]
            l[j] = l[j+1]
            l[j+1] = temp
            temp = b[j]
            b[j] = b[j+1]
            b[j+1] = temp
print(l)
print(b)
d =0         
def quest(n,l,b,e,d):
    for i in range(n):
        if e>l[i]:
            e += b[i]
            d+=1
            print("You have successfully defeated ",i+1,"Monster")
            print("Your Total Power is ",e)
            print("Your Defeat count is ",d)
            print("<====================>")
        else:
            print("You have been defeated ")
            print("Your Defeat count is ",d)
            break
quest(n,l,b,e,d)
            