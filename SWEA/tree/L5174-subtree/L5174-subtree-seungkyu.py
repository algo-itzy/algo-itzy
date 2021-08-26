import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):

    E, N = map(int, input().split())
    numbers = list(map(int, input().split()))
    child = [[] for _ in range(E+2)]

    for i in range(0, 2*E, 2):
        a, b = numbers[i], numbers[i+1]
        child[a].append(b)  # 무조건 a가 parent

    ans = 1
    stack = child[N]  # N의 자식 값들 넣어줌
    while stack:  # 스택이 빌 때까지 진행
        cur = stack.pop()  # 현재 위치
        ans += 1
        stack += child[cur]  # 연결된 자식 값들 더해줌

    print(f'#{test_case} {ans}')
