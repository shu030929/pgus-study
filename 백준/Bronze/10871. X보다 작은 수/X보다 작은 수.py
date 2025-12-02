num,find = map(int,input().split())



num_list = list(map(int, input().split()))

count = []

for i in range(len(num_list)):
    if find > int(num_list[i]):
        count.append((num_list[i]))
        

print(*count)