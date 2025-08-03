#checking word1 is right rotation of word2

#>>>> without function<<<<

word1 =input("Enter word1: ")
word2 =input("Enter word2: ")

mid = len(word1)//2

c1 = word1[0:mid]
c2 = word1[mid:]

new = c2 + c1

if new == word2:
    print("1")

# >>>> with function <<<<

# def isRightRotation(Word1,word2):
#     if len(Word1) != len(word2):
#         return -1
#     if word2 in (Word1 +word2):
#         return 1
#     return -1

# def main():
#     word1 =input().strip()
#     word2 =input().strip()
#     result = isRightRotation(word1,word2)
#     print(result)

# if __name__ == "__main__":
#     main()