# n -> no of  monkey
# k -> can eat k bananas
# j -> can eat j peanuts

# m bananas & p peanuts are offered


def monkeytest(n,m,p,k,j):
    z =n
    while m > 0 and p > 0 :
        if n == 0:
            n = z
        # eat banas
        if(m >= k):
            m = m -k
            n-=1
            print("m left:",m , "p left:",p , " number of monkeys: ",n)
            # banana 
        
        elif(p>= j):
            p = p - j
            n -=1
            print("m left:",m , "p left:",p , " number of monkeys: ",n)
            
        # leftover number of stuff not enough
        elif(( p > 0 or m >0)):
            p =0
            m =0 
            n = n-1
            print("m left:",m , "p left:",p , " number of monkeys: ",n)

    print(n)
    return n



monkeytest(
    5,31,5,3,2
)

