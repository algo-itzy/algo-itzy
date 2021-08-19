import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):

    N = int(input())
    numbers = list(map(int, input().split()))

    # 산 날 파는 것은 무의미, 사는 날과 파는 날 구분
    # 기준 숫자보다 작은 숫자 나오면 파는 것, 큰 숫자 나오면 업뎃
    # 역탐색..쉽게 하기위해 reverse해서 사용
    numbers.reverse()
    start = total = 0

    for idx in range(len(numbers)):
        
        if numbers[start] > numbers[idx]:  # 파는 것
            total += numbers[start]-numbers[idx]
        elif numbers[start] < numbers[idx]:  # 큰 수로 업데이트
            start = idx

    print(f'#{test_case}', total)
