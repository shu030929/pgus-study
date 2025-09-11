def solution(myString):
    answer = ''
    comp = ord("l")
    print(comp)
    
    for i in myString:
        if ord(i)<comp :
            answer += "l"
        else:
            answer += i
    
    
    return answer