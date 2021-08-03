'''
층과 거리 계산하는 것은 간단,
층이 꼭대기일 경우의 수를 따로 처리해주어야 함(이것 때문에 한 번 틀림)
'''
import sys

def solve():
    input = sys.stdin.readline
    t = int(input())

    for _ in range(t):
        h, w, n = map(int, input().split())
        floor = n % h
        dist = (n//h) + 1

        # 층이 꼭대기인 경우를 따로 생각
        if floor == 0:
            floor = h
            dist = (n//h)
        # 호수가 10호 미만일 경우와 이외의 경우로 나눠서 생각
        if dist < 10:
            print(f'{floor}0{dist}')
        else:
            print(f'{floor}{dist}')
        
if __name__ == "__main__":
    solve()
