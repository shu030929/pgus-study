def solution(my_string, index_list):
    answer = ''
    num = 0
    
    for i in range(len(index_list)):
        num = index_list[i]
        answer += my_string[num]
    
    
    
    return answer