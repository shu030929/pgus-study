def solution(my_str, n):
    answer = []
    
    
    if len(my_str)%n != 0:
        count = len(my_str)//n +1
    else:
        count = len(my_str)//n
    
    
    start = 0
    end = n
    for i in range(count):
        answer.append(my_str[start:end])
        start +=n
        end+=n
        
        
        
    
    
    return answer