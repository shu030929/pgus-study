def solution(arr):
    answer = [[]]
    row = 0
    col = 0
    
    for i in range(len(arr)):     
        row += 1   
        for j in range(len(arr[i])):
            col += 1
    
    col = col//row
    # 세로 = row 
    # 가로 = col
    print("row =",row)
    print("col =",col)
    
    
    if row>col:
        cnt = row-col
        while cnt != 0:
            for i in range(len(arr)):
                arr[i].append(0)
            cnt -= 1
            
    elif col>row:
        cnt = col-row
        while cnt != 0:
            plus = [0 for _ in range(col)]
            arr.append(plus)
            cnt -=1
    
    
    
    return arr