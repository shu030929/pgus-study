def solution(numLog):
    answer = ''
    look = ''
    
    
    for i in range(1,len(numLog)):
        look = numLog[i-1]
        change = numLog[i] - look
        
        if change == 1:
            answer += "w"
        elif change == -1:
            answer += "s"
        elif change == 10:
            answer += "d"
        elif change == -10:
            answer += "a"
        
    return answer