import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    N, M, L = map(int, input().split())
    numbers = list(map(int, input().split()))

    for _ in range(M):
        cmd = input().split()

        if cmd[0] == 'I':
            numbers.insert(int(cmd[1]), int(cmd[2]))
        elif cmd[0] == 'D':
            numbers.pop(int(cmd[1]))
        elif cmd[0] == 'C':
            numbers[int(cmd[1])] = int(cmd[2])

    result = numbers[L] if len(numbers) > L else -1
    print(f'#{t} {result}')
