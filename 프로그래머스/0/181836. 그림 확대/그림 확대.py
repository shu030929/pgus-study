def solution(picture, k):
    answer = []

    
    for i in range(len(picture)): # 
        keep = ""
        for j in picture[i]: # 각
            keep = keep + j *k
        answer.extend([keep] * k)
        
    
    return answer