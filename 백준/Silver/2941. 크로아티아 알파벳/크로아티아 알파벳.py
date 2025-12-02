maps = ['c=', 'c-','dz=','d-','lj','nj','s=','z=']
count = 0

came = str(input())

for i in range(len(came)): # 하나하나 볼꺼임
    
    for j in maps:
        if came.find(j) != -1: #찾으면 
            came = came[:int(came.find(j))] +","+ came[int(came.find(j))+len(j):]
            break
          



print(len(came))