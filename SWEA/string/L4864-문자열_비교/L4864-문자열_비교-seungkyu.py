import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T+1):

    N = input()
    M = input()

    ans = (1 if N in M else 0)

    print(f'#{test_case} {ans}')