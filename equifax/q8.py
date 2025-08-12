# accepting chemicals in the format [12 34 73 86] and returning sum of the chemicals that give max product in this 8+6=14

n = int(input("Enter the size: "))
s = input("Enter the chemicals: ").strip().split()
s = [int(x) for x in s]
if len(s) != n:
    print(f"Error: Expected {n} chemicals but got {len(s)}")
    exit()
max = 0
sum =0
for i in range(n):
    c1 = s[i]//10
    c2 = s[i]%10
    if c1*c2 > max:
        max = c1*c2
        sum = c1+c2
        
print(sum)