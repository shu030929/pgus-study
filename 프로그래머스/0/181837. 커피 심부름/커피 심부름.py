def solution(order):
    answer = 0
    
    # 아메리카노 : 4500
    # 카페라때 : 5000
    # 아무거나 : 4500(아메리카노)
    
    for i in range(len(order)):
        if order[i].find("americano") != -1:
            answer += 4500
        elif order[i].find("anything") != -1:
            answer += 4500
        elif order[i].find("cafelatte") != -1:
            answer += 5000
        
    
    return answer