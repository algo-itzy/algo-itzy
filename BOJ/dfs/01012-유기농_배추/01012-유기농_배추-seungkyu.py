import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def solve():
    t = int(input())

    for _ in range(t):
        m, n, k = map(int, input().split())
        vegetable_list = [[0 for _ in range(m)] for _ in range(n)]
        # input값 리스트에 저장
        for _ in range(k):
            x, y = map(int, input().split())
            vegetable_list[y][x] = 1

        ans = 0 # 1로 묶인 덩어리 저장 변수
        # x = 0, y = 0 에서 x를 1씩 증가, 한줄 끝나면 y를 1씩 증가하며 탐색
        for x in range(n):
            for y in range(m):
                if vegetable_list[x][y] == 1:
                    ans += 1
                    dfs(x, y, m, n, vegetable_list)
        print(ans)
                            
def dfs(x, y, m, n, vegetable_list):
    # x, y축 이동(상하좌우) 관련 변수
    dir_x = [1, -1, 0, 0]
    dir_y = [0, 0, 1, -1]
    for i in range(4): 
        x = x + dir_x[i]
        y = y + dir_y[i]
        
        if (0 <= x < n) and (0 <= y < m):
            if vegetable_list[x][y] == 1:
                vegetable_list[x][y] = 0
                dfs(x, y, m, n, vegetable_list)

if __name__ == "__main__":
    solve()
