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

if __name__ == "__main__":
    # stages = [2, 1, 2, 6, 2, 4, 3, 3]
    stages = [4, 4, 4, 4, 4]
    solution(4, stages)

# git commit -m "code: Solve programmers 실패율 (yoonbaek)"