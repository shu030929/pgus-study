def solution(n, w, num):
    ## n = 택배 개수 / w = 가로 개수
    
    temp = [[] for _ in range(w)]
    print("temp=",temp)
    
    count = 0 #인덱스
    value = 1 #박스 번호
    term = 1
    
    while value != n+1: #박스 번호가, 마지막 박스 번호까지
        if value%w == 0: # 인덱스가 배열수일때
            temp[count].append(value)
            term = -term
            value += 1
            
        elif term == 1: #정방향
            temp[count].append(value)
            value += 1 
            count += 1 
        
        elif term == -1: #역방향
            temp[count].append(value)
            value += 1 
            count -= 1 
    
    print("temp=",temp)
    
    for x in range(w) :
        if num in temp[x] :
            print(temp[x])
            print(temp[x].index(num))
            print(len(temp[x]))
            
            print("---")
            
            print(len(temp[x]) - temp[x].index(num) - 1)
            return (len(temp[x]) - temp[x].index(num) )
    

    return 0
        
