def solution(code):
    answer = ''
    mode = 0
    
    for i in range(len(code)):
        # i = index
        if code[i] == "1" and mode == 0:
            mode = 1
        elif code[i] == "1" and mode == 1:
            mode = 0
        
        
        elif mode == 0 and code[i] != "1" and i%2 == 0:
            answer = answer + code[i]

        
        elif mode ==1 and code[i] != "1" and i%2 != 0:
            answer = answer +code[i]
            
    while not answer:
        return "EMPTY"
            
        
    
    return answer