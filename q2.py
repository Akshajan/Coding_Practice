
def fib(n):
    if  n==1 or n==2:
        return 1
    else:
        return fib(n-2)+fib(n-1)
    
def isPrime(num):
    if num<=1:
       return False
    for i in range(2,num//2+1):
        if num%i ==0:
            return False
    return True
   
def nthPrime(n):
    if n<1:
        return None
    count = 0
    num =2
    while count < n:
        if isPrime(num):
            count +=1
        num +=1
    return num-1
    
def series(n):
    if n%2 == 1:
        return fib(n//2+1)
    else:
        return nthPrime(n/2)
    
for i in range(20):
    print(i,":",series(i))