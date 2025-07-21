n=int(input("Enter monsters:"))
exp=int(input("Enter initial experience"))
pow=[]
bon=[]
for i in range(n):
    pow.append(int(input("Enter power:")))
for i in range(n):
    bon.append(int(input("Enter Bonus:")))

for i in range(n):
    for j in range(n-1):
        if pow[j]>pow[j+1]:
            temp=pow[j]
            pow[j]=pow[j+1]
            pow[j+1]=temp
            temp=bon[j]
            bon[j]=bon[j+1]
            bon[j+1]=temp
print(pow)
print(bon)

de=0
for i in range (n):
    if(exp>=pow[i]):
        exp=exp+bon[i]
        de=de+1
print(de)