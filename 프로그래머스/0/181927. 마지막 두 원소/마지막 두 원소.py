def solution(num_list):
    answer = num_list

    last = num_list[-1]
    
    if last > num_list[-2]:
        answer.append(last-num_list[-2])
    else:
        answer.append(last*2)
    
    
    
    return answer