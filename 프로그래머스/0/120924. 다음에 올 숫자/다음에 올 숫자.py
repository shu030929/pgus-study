def solution(common):
    # 등차인지 등비인지 먼저 판별
    if common[1] - common[0] == common[2] - common[1]:
        # 등차수열
        diff = common[1] - common[0]
        return common[-1] + diff
    else:
        # 등비수열
        ratio = common[1] // common[0]
        return common[-1] * ratio
