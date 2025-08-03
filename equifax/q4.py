#program to count numbers of duplicate characters

a = list(input("String: "))
matches ={}
for char in a:
    if char in matches:
        matches[char] +=1
    else:
        matches[char] =1
                
print("Duplicate characters are :")  
            
for char,count in matches.items():
    if count >1:
         print(f"characters {char} occurs {count} times")