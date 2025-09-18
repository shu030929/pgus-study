def solution(quiz):
    answer = []
    
    
    for each in range(len(quiz)):
        cal = quiz[each].split()
        
        val1 = cal[0]
        val2 = cal[2]
        op = cal[1]
        ans = cal[-1]
        
        if op == "+":
            temp = int(val1) + int(val2)

            if int(temp) == int(ans):
                answer.append("O")
            else:
                answer.append("X")
            
        elif op == "-":
            temp = int(val1) - int(val2)
            if int(temp) == int(ans):
                answer.append("O")
            else:
                answer.append("X")
            
    
    return answer