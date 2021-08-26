import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):

    N, M, L = map(int, input().split())
    numbers = list(map(int, input().split()))

    for _ in range(M):
        cmd = input().split()

        if cmd[0] == 'I':
            numbers.insert(int(cmd[1]), int(cmd[2]))
        elif cmd[0] == 'D':
            del numbers[int(cmd[1])]
        elif cmd[0] == 'C':
            numbers[int(cmd[1])] = int(cmd[2])
        
    if L < len(numbers):
        print(f'#{test_case}', numbers[L])
    else:  # 인덱스 벗어날 때
        print(f'#{test_case}', -1)
