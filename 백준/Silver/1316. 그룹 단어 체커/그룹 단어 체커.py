num = int(input())
strings = []
no = 0


for i in range(num):
    strings.append(input())
# 각 문자열이 배열에 넣어져있음



# 문자열 하나씩 볼꺼임

for string in strings:
    stack = [0]
    
    for i in string: # 한글짜
        


        if stack[-1] == i: #방금꺼랑 똑같으면
            stack.append(i) #수락
            #print("1번문 수락:",stack)
        elif stack[-1] != i and (i not in stack): #방금꺼랑 다른거면
            stack.append(i) #수락
            #print("2번문 수락:",stack)
        elif (stack[-1] != i) and (i in stack): #방금꺼랑 다른데, 이미 스택에 있으면 
            no += 1
            #print("중복 발견:",i )
            break
            
        
print(num-no)