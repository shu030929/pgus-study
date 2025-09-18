def solution(array):
    answer = []
    
    big = max(array)
    answer.append(big)
    
    for i in range(len(array)):
        if array[i] == big:
            answer.append(i)
    
    
    
    
    
    return answer