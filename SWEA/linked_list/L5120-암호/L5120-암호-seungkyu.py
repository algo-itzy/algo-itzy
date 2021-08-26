import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):

    N, M, K = map(int, input().split())
    numbers = list(map(int, input().split()))
    idx = 0
    for _ in range(1, K+1):  # K번 반복

        idx = (idx+M) % N  # idx 업데이트

        if idx == 0:  # 맨 뒤에 합친 값을 추가
            sum_num = numbers[idx]+numbers[idx-1]
            numbers.append(sum_num)
            idx = -1
        else:  # 인덱스 이용 insert
            sum_num = numbers[idx]+numbers[idx-1]
            numbers.insert(idx, sum_num)
        N += 1

    print(f'#{test_case}', *numbers[-1:-11:-1])  # 역순 출력
