n = int(input("Enter the n:"))
b = [input(f"Enter the color {i+1}: ") for i in range(n)]
z={}

for i in b:
    if i not in z :
        z[i]=1
    else:
        z[i]=z[i]+1
    
for i in z:
    if(z[i]%2!=0):
        print(i,"count is",z[i])
        break
else:
    print("All are even")
