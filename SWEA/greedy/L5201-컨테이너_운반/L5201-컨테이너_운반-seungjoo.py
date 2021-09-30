# git commit -m "code: Solve swea L5201 컨테이너 운반 (seungjoo)"
for test in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    w = list(map(int, input().split()))
    t = list(map(int, input().split()))
    t.sort(reverse=True)
    w.sort(reverse=True)
    answer = 0
    left = 0
    for truck in t:
        while left < N and truck < w[left]:
            left += 1
        if left == N: break
        answer += w[left]
        left += 1
        
    print(f'#{test} {answer}')