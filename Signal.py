
def Signal():
    # nums = list(map(int, input().strip()))
    s = list(input())
    nums = [int(x) for x in s]
    matches={}
    for n in nums:
        if n in matches:
            matches[n]+=1
        else:
            matches[n]=1
   
   # making list of keys
    keys = list(matches.keys())

    # bubble sort keys
    n = len(keys)
    for i in range(n):
        for j in range(0, n-i-1):
            if keys[j] > keys[j+1]:
                keys[j], keys[j+1] = keys[j+1], keys[j]

    # create new sorted dictionary
    sorted_dict = {}
    for k in keys:
        sorted_dict[k] = matches[k]
        
    print(sorted_dict)
    
    l = [value for key,value in sorted_dict.items()]
    r = " ".join(str(v) for v in l)
    print(r)
             
Signal()