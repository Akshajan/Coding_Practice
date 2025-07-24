l=[]
for i in range(2,7,1):
    l.append(i)
    print(i,end=" ")
print("")
# normal
def a1(x):
    return x%2 == 1
# lambda
a = lambda x: x%2==1
# filter bool(lambda) , arr
# this gives obj conv to list
print(list(filter(a,l)))

print(a(35))
print(a1(35))