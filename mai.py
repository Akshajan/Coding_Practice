import random
# a = [(random.randint(0,19) ,random.randint(0,19) )for i in range(4)]
a =['1  2 ', ' 2 3']
#a = [(input()) for i in  range(2)]
for i in range(2):
   
    z = ( a[i].strip().split())
    print(list(filter(lambda x: x!="",z)))
    
# print(list(filter(lambda x: x!="",a)))
# a.sort(key=lambda y:y[0])

# print(a)
# str = input("Enter the sequence:")
# for i in str:
#     print
    
# 97 - 122
# after_shift =ord("z") -  ord("a") +1
# print("aftrshift",after_shift)
# print(ord("a"))
# print("=====")
# print(ord("z"))
# print(ord("z")+1)

# print((ord("d")-ord("a")+1)%26 + 97)
# print(chr((ord("d")-ord("a")+1)%26 + 97))

# aaaaa = ["2","2","3"]
# # print(aaaaa.strip().split(" "))
# # aa = (aaaaa.split(" "))

# print(list(filter(lambda x: int(x)%2 !=0 , aaaaa)))

# # "" -> false  sdsd ->  true 