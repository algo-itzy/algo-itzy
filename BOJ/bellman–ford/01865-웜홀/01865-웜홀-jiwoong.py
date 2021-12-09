# git commit -m "code: Solve boj 01865 웜홀 (jiwoong)"
import sys

input = sys.stdin.readline


def bellman_ford():
    dist = [10000 * N] * (N + 1) 
    dist[1] = 0 

    for i in range(N):
        for sn, en, t in edges:
            if dist[sn] + t < dist[en]:
                dist[en] = dist[sn] + t
                if i == N - 1: 
                    return 'YES'
    return 'NO'


T = int(input())
for _ in range(T):
    N, M, W = map(int, input().split())
    edges = []  
    for _ in range(M):
        S, E, T = map(int, input().split())
        edges.append((S, E, T))
        edges.append((E, S, T))
    for _ in range(W):
        S, E, T = map(int, input().split())
        edges.append((S, E, -T)) 
    print(bellman_ford())
