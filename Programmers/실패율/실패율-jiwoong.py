# git commit -m "code: Solve programmers 실패율 (jiwoong)"
def solution(N, stages):
    result = {}
    num = len(stages)  # 총 인원
    for i in range(1, N + 1):
        if num == 0:
            result[i] = 0
        else:
            cnt = stages.count(i)  # 실패 인원
            result[i] = cnt / num
            num -= cnt
    result = sorted(result, key=lambda x: result[x], reverse=True)
    return result
