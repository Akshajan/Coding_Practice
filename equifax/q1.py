#finding count of a specific character in a string

s = list(input("Enter the string: "))
c = (input("Enter the compare string: "))
count=0
for i in s:
    if i == c:
        count +=1

print(count)
