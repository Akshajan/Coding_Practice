#program to find mirrored characters

s = list(input("Enter a string: "))
n = len(s)
matches ={}
for i in range(n//2):
    if s[i] == s[n-i-1]:
        char = s[i]
        if char in matches:
            matches[char]+=1
        else:
            matches[char] = 1

for char,count in matches.items():
    print(f"character {char} matched {count} times")
            
