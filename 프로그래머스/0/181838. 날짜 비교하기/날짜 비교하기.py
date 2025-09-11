def solution(date1, date2):
    for i in range(3):
        if date1[i] < date2[i]:
            return 1
        elif date1[i] > date2[i]:
            return 0
    return 0   # 전부 같을 경우
