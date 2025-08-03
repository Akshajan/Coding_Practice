#print prime numbers for given range

def isPrime(n):
    if n<2:
        return False
    for i in range(2,n//2+1):
        if n%i == 0:
            return False
    return True

def printPrime(num):
    if num<1:
        return None
    n=0
    while n<=num:
        if isPrime(n):
            print(n,end="\t")
        n+=1
num = int(input("Enter the range: "))
printPrime(num)