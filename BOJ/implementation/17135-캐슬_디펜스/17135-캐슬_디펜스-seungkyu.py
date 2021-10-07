# git commit -m "code: Solve boj 17135 캐슬 디펜스 (seungkyu)"
import sys
input = sys.stdin.readline


# x, y(궁수 위치)에 대하여 가장 가까운 점, 거리 구하기
def cal_dist(x, y):
    dist = [float('inf'), N, M]
    for i in range(N):
        for j in range(M):
            if mat[i][j]:
                tmp = abs(x-i)+abs(y-j)
                if tmp <= dist[0] and tmp <= D:
                    if tmp == dist[0] and dist[2] > j:
                        dist[0] = tmp
                        dist[1] = i
                        dist[2] = j
                    elif tmp < dist[0]:
                        dist[0] = tmp
                        dist[1] = i
                        dist[2] = j
    return dist


# 궁수 위치 브루트포싱
def comb(nums, n):
    ret = []
    if n > len(nums): return ret

    if n == 1:
        for i in nums:
            ret.append([i])
    elif n > 1:
        for i in range(len(nums)-n+1):
            for temp in comb(nums[i+1:], n-1):
                ret.append([nums[i]] + temp)

    return ret

N, M, D = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
nums = [i for i in range(M)]
ans= 0

for positions in comb(nums, 3):
    cnt = 0
    mat = [item[:] for item in matrix]  # slicing copy
    for i in range(N):  # 맨 밑에 줄 빼고 맨 윗줄에 0... 집어넣는 것 반복
        
        dists = []
        for pos in positions:
            dists.append(cal_dist(N, pos))
        for dist in dists:
            if dist[1] == N and dist[2] == M:
                continue
            elif mat[dist[1]][dist[2]]:
                mat[dist[1]][dist[2]] = 0
                cnt += 1

        mat.pop()
        mat = [[0]*M] + mat

    ans = max(ans, cnt)

print(ans)
