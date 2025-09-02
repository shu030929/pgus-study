def solution(arr, queries):
    answer = []
    
    for s, e, k in queries:
        temp = []  # 쿼리마다 새로 초기화!
        
        for i in range(s, e+1):  # 인덱스 s~e만 확인
            if arr[i] > k:       # k보다 큰 값만
                temp.append(arr[i])
        
        if temp:  # 후보가 있으면 최소값
            answer.append(min(temp))
        else:    # 없으면 -1
            answer.append(-1)
    
    return answer
