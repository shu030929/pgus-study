def solution(s1, s2):
    answer = 0
    
    
    for i in range(len(s1)):
        print("i=",i)
        maxi = len(s2)-1
        
        while maxi >= 0:
            print(s1[i])
            print(s2[maxi])
            if s1[i] == s2[maxi]:
                answer += 1
            
            maxi -=1
    
    
    
    return answer