#find the count of characters that are not repeated in the string

s = input("Enter the string: ")
matches ={}
for char in s:
    if char in matches:
        matches[char] +=1
    else:
        matches[char] =1
                
# l=[]
# for char,count in matches.items():
#     if count ==1:
#         l.append(char)

# collecting non-repeating characters
l = [char for char,count in matches.items() if count == 1]

print("Non-repeating characters are :",' '.join(l))  
print(f"Total count is {len(l)}")