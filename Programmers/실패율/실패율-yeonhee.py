def solution(N, stages):
    user_list = [0]*(N+2)

    for stage in stages:
        user_list[stage] += 1

    failure_rate = {}

    for i in range(1, N+1):
        challengers = sum(user_list[i:])
        failure_rate[i] = user_list[i] / challengers if challengers else 0

    answer = sorted(failure_rate, key=lambda x: (-failure_rate[x], x))

    return answer
