

compare = [1,1,2,2,2,8] # 비교대상
chess = list(map(int,input().split())) #현재 체스
ans = []


for i in range(len(compare)):
    
    if compare[i] == chess[i]:
        ans.append(0)
    elif compare[i] > chess[i]:
        ans.append(int(compare[i])- int(chess[i]))
    else:
        ans.append(-(int(chess[i]) -int(compare[i])))
        
        
print(*ans)