score = []
total = 0
maps = {"A+":4.5, "A0": 4.0, "B+":3.5, "B0":3.0, "C+":2.5, "C0":2.0, "D+":1.5, "D0": 1.0, "F":0,"P":7 }
allSco = 0
todiv = 0 #학점의 총 합

for i in range(20):
    score.append((input().split()))
    
for each in score: #한줄
        
    alp = each[-1] #등급
    sco = each[-2] #학점
    allSco += float(each[-2])
        
    if maps.get(alp) == 7: #p일 경우
        todiv += float(sco)
        

    else: # p가 아닐경우
        alpS = maps.get(alp) #등급 점수화
        total += float(sco)*float(alpS)
        

print(total/(allSco-todiv))


