string = str(input())
string = string.upper()

count = [0]*26

for i in range(len(string)):
    order = (ord(string[i])) - 65
    count[order] += 1 
    

maxCount = (max(count))

if count.count(maxCount) > 1:
    print("?")
else:
    print(chr(count.index(maxCount) + 65))