n = int(input("input number of colors of balloons:"))
l=[]
for i in range(n):
    l.append(input("Enter the color:")) 
c=[] 
found_odd = False
for i in range(n): 
    count = 0  
    for j in range(n):
        if l[i] == l[j] :
           count +=1
        
    if count%2 == 1:
        print(l[i],"Count :",count)
        found_odd = True
        break
    
if not found_odd:
    print("All are even")     
