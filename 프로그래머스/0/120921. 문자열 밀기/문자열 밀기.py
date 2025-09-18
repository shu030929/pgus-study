def solution(A, B):
    answer = 0
    count = 0

    if A == B:
        return 0
    
    for i in range(len(A)): # 한바퀴 돌려볼꺼임
        print(A)
        count +=1
        pop = A[-1] # 맨 뒤에꺼 pop
        A = pop + A[0:len(A)-1]
        
        
        if A.find(B) != -1: # 찾으면
            return count
        
    
    return -1