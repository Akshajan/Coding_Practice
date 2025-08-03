#program to count numbers of unique characters

a = list(input("String: "))
n = len(a)
count=0
for i in range(n):
    for j in range(i):
        if a[i] == a[j]: #this if loop checks the characters are unique, for j in range(0) the loop won't run so count will be increased to 1
            break # if any of the characters repeats the break statements activates and exit from inner j loop and count won't increase
    else: #if any of the characters are not equal we exit the if statement and go to else part
        count +=1# so for every j loop we can atmost increase count value by 1
print(count)