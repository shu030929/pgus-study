def solution(ineq, eq, n, m):
    answer = 0
    cal = ""
    
    cal = ineq+eq
    
    if cal == "<=":
        if (n <= m) is True:
            return 1

    
    elif cal == ">=":
        if (n >= m) is True:
            return 1

        
    elif cal == ">!":
        if (n>m) is True:
            return 1
        
    elif cal == "<!":
        if (n<m) is True:
            return 1
    
    else:
        return 0
    
    return answer