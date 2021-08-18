import sys
import numpy as np

sys.stdin = open('input.txt')


def list_to_str(lst):
    return ''.join(map(str, lst))


for t in range(1, int(input())+1):
    n = int(input())
    mtx = [list(map(int, input().split())) for _ in range(n)]
    mtx = np.array(mtx)

    mtx_90 = np.rot90(mtx, -1)
    mtx_180 = np.rot90(mtx_90, -1)
    mtx_270 = np.rot90(mtx_180, -1)

    print(f'#{t}')

    for i in range(n):
        print(*map(list_to_str, (mtx_90[i], mtx_180[i], mtx_270[i])))

"""
예전에 공부했던 넘파이가 생각나서 써봤습니다.
np.rot90()으로 90도 회전이 쉽게 가능합니다.
"""
