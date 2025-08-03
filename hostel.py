# n number of students
# random order of students
#prime > composite
#less prime (pp)
#greater composite(cc)

a = list("Kkunjkhahorin")
print(a)
prime =[]
comp =[]

def isprime(n):
    if n<2:
        return False
    if n==2:
        return True
    for i in range(2,n//2+1):
        if n%i == 0:
            return False
    return True
prime = []
composite = []
for item in a:
    n= ord(item)  
    if(isprime(n)):
        prime.append(item)
    else:
        composite.append(item)
           
prime.sort()
composite.sort()
a= prime + composite[::-1]

print("".join(a))

    