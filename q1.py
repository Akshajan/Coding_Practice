#Total m-bananas p-peanuts
#one monkey can eat k bananas or j peanuts
# calculate remaining monkeys on the tree 

def monkey(n,m,p,k,j):
    z=n
    while m>0 and p>0:
        if n == 0:
            n=z
        if(m>=k):
            m -= k
            n -= 1
            print("m Left:",m,"p Left:",p,"n Left:",n)
        elif(p>=j):
            p -= j
            n -= 1
            print("m Left:",m,"p Left:",p,"n Left:",n)
        else:
            m=0
            p=0
            n-=1
            print("m Left:",m,"p Left:",p,"n Left:",n)
    
monkey(5,31,10,5,3)
          
    
             
            
        
