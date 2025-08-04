#find the count of the given word from sequence of input words

seq = input("Enter the sequence of string: ").strip().split()
comp = input("Enter the word:")
count =0
for i in seq:
    if i==comp:
        count+=1
print(count)