import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):

    N, M = map(int, input().split())

    numbers = []
    for _ in range(M):
        nums = list(map(int, input().split()))
        for idx, num in enumerate(numbers):
            if nums[0] < num:
                numbers[idx:idx] = nums  #  idx:idx 배열 중간에 값 넣기
                break
        else:
            numbers += nums  # 끝에 요소들 붙이기

    print(f'#{test_case}', *numbers[-1:-11:-1])
