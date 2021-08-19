import sys
sys.stdin = open('input.txt')


def rotate_90(mtx):
    return [row[::-1] for row in zip(*mtx)]


def list_to_str(lst):  # 출력부를 위한 함수
    return ''.join(map(str, lst))


for t in range(1, int(input())+1):
    n = int(input())
    mtx = [list(map(int, input().split())) for _ in range(n)]

    mtx_90 = rotate_90(mtx)
    mtx_180 = rotate_90(mtx_90)
    mtx_270 = rotate_90(mtx_180)

    print(f'#{t}')

    for i in range(n):
        print(*map(list_to_str, (mtx_90[i], mtx_180[i], mtx_270[i])))

"""
zip 정도는  날로먹는 풀이는 아니라고 생각합니다....
"""
