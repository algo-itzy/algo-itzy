import sys
sys.stdin = open('input.txt')


def rotate_90(numbers_t):
    rot_90 = []
    for num in numbers_t:  # 배열 그대로
        num = list(num)
        num.reverse()  # 거꾸로 읽기
        rot_90.append(num)
    
    return rot_90


def rotate_180(numbers):
    rot_180 = []
    numbers.reverse()  # 배열 뒤집기
    for num in numbers:
        num.reverse()  # 거꾸로 읽기
        rot_180.append(num)

    return rot_180


def rotate_270(numbers_t):
    rot_270 = []  
    numbers_t.reverse()  # 배열 뒤집기
    for num in numbers_t:
        num = list(num)
        rot_270.append(num)

    return rot_270

T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    numbers = [list(map(int, input().split())) for _ in range(N)]
    numbers_t = list(zip(*numbers))  # 세로로 배열 읽기
    
    rot_90 = rotate_90(numbers_t)  # 90도 회전
    rot_180 = rotate_180(numbers)  # 180도 회전
    rot_270 = rotate_270(numbers_t)  # 270도 회전

    # 출력 형식 맞추기 위해서 zip 사용 후 for문 돌면서 print
    answers = list(zip(rot_90, rot_180, rot_270))
    print(f'#{test_case}')
    for ans in answers:
        for i in ans:
            print(*i, sep='', end=' ')
        print()
