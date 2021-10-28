def solution(N, stages):
    fail_rates = []

    arrived = [0]*(N+2)

    for stage in stages:
        arrived[stage] += 1
    
    for i in range(1, N+1):
        total = sum(arrived[i:])
        fr = arrived[i] / total if total != 0 else 0
        fail_rates.append((i, fr))

    fail_rates.sort(key=lambda x: x[1], reverse=True)

    answer = []
    for fr in fail_rates:
        answer.append(fr[0])

    return answer

# git commit -m "code: Solve programmers 실패율 (yoonbaek)"