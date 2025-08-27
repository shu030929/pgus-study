def solution(num_list):
    answer = 0
    odd = ""
    even = ""
    
    
    for i in range(len(num_list)):
        if int(num_list[i])%2 == 0:
            even = even + str(num_list[i])

        else:
            odd = odd + str(num_list[i])
            
            
        
    
    
    return int(odd) + int(even)