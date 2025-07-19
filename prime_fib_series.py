# odd fib
# even prime


    
def is_prime(n):
    if n == 2: return True
    if n > 2 :
        
        for i in range(2,n//2+1):
            if n % i == 0:
                return False
        return True
    else:
        # less than 2
        return False

def nth_prime(n):
    # nth number
    if n <1:
        print("shut the fuck up  nigga")
        return None
    count = 0
    num = 1
    
    while count != n:
        # ayal chodiche nth number nik kitti break
        if(is_prime(num)):
            count += 1
            if count == n:
                return num
        num +=1
        
            
print(nth_prime(3))     
    
            
def fib(n):
    
    if n ==1:
        return 1
    if n == 2:
        return 1
    return fib(n-1)+fib(n-2)
        
def series(N):
    # odd
    if( N%2 == 1):
        return fib(N//2+1)
    # even
    else:
        return nth_prime(N/2)

for i in range(15):
    print(i ," : ",series(i))