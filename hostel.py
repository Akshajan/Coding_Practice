# n number of students
# random order of students
#prime > composite
#less prime (pp)
#greater composite(cc)

a = list("kku")
print(a)
prime =[]
comp =[]
#  n
# n < 2 false
# n == 2 true
# # for  i  2->n
        # n%i break
# # true
def isprime(n):
    if n<2:
        return False
    if n==2:
        return True
    for i in range(2,n//2+1):
        if n%i == 0:
            return True
            break
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

    