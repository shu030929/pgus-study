def solution(num, total):
    answer = []
    base = []
    do = 0
    
    mid = total//num # 중간값  
    base = [0 for _ in range(num)] #기본 개수대로 생성하기
    if num%2 != 0: # 가운데 범위에 그 숫자 넣기
        base[num//2] = mid
        cnt = num//2
        cnt2 = num//2
    else:
        base[num//2-1] = mid
        cnt = num//2 -1
        cnt2 = num//2 -1
        
    while cnt > 0:
        do += 1
        cnt -= 1
        base[cnt] = mid-do
        
    
    do = 0
    print("while문 이전",cnt2)
    print(do)
    while cnt2 < num-1:
        do += 1
        cnt2 += 1
        base[cnt2] = mid+do
        
        

    
    answer = base
    
    return answer