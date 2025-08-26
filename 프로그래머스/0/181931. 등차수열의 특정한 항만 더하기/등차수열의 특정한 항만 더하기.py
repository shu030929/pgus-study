def solution(a, d, included):
    answer = 0
    
    for i in range(len(included)):
        
        if included[i] == True and answer == 0:
            answer += (a + (d)*i)
        

        elif included[i] == True and answer != 0:
            answer += (a + (d)*i)
        
            
        
    return answer