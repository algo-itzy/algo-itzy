import sys
import math
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T+1):
    
    N = int(input())
    n = N // 10
    total = 0
    for i in range(n//2 + 1):
        total += (math.factorial(n-i) // (math.factorial(i) * math.factorial(n-2*i))) * (2**i)

    print(f'#{test_case} {total}')