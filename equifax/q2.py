#accepting a sequence of characters in a single in a space separated format ie[a k s h a j a n] 
# and comparing with a i/p char to find it's count in the given sequence

n = int(input("Enter the size: "))
#s = [(input("Enter "+str(i) +":")) for i in range(n)]
#s= [(input(f"Enter {i}:")) for i in range(n)]
s = input("Enter a string: ") .strip().split()
k = input("Enter the char: ")
count=0
for i in range(n):
    if s[i]==k:
        count +=1

print(f"The character {k} occur in the string {count} times")
