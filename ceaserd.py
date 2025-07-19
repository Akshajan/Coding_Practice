str = input("Enter the sequence:")
key = int(input("enter the Shift Value:"))
enc=[]
for i in str:
    if i.islower():
        enc.append(chr((ord(i)-ord("a")+key)%26 + ord("a")))
    elif i.isupper():
        enc.append(chr((ord(i)-ord("A")+key)%26 + ord("A")))
    elif('0'<=i<='9'):
        enc.append(chr((ord(i)-ord("0")+key)%10 + ord("0")))
    else:
        enc.append(i)
        
print(" ".join(enc))
        
        
    
        