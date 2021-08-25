import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    n, m, k = map(int, input().split())
    numbers = list(map(int, input().split()))
    idx = m

    for _ in range(k):
        if not idx:
            numbers.append(numbers[idx - 1] + numbers[idx])
            idx -= 1
        else:
            numbers.insert(idx, numbers[idx - 1] + numbers[idx])
        idx = (idx + m) % len(numbers)

    print(f'#{t}', *numbers[::-1][:10])
