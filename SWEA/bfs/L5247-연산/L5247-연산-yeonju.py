# 3번 테스트 케이스에서 무한루프에 빠져서 나오지 못하고 있습니다,,, ㅠ-ㅠ

def solution(num, cnt): # 연산 과정을 거친 현재 값, 연산 횟수
    global min_cnt

    if num == m: # m의 값과 같게 되면
        if cnt < min_cnt:
            min_cnt = cnt
        return min_cnt

    if cnt > min_cnt:
        return

    solution(num + 1, cnt + 1)
    if tc == 2:
        print(num)
    solution(num - 1, cnt + 1)
    solution(num * 2, cnt + 1)
    solution(num - 10, cnt + 1)


for tc in range(int(input())):
    n, m = map(int, input().split())

    min_cnt = 1000000000
    solution(n, 0) # 자연수 n에서 연산 시작, 초기 연산 횟수 0으로 초기화
    print(f'#{tc+1} {min_cnt}')

# git commit -m "code: Solve swea L5247 연산 (yeonju)"