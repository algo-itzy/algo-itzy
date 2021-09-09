from sys import stdin
from collections import deque

rd = stdin.readline

d = lambda n: (2*n) % 10000
s = lambda n: 9999 if n == 0 else n-1
l = lambda n: n%1000*10+n//1000
r = lambda n: n//10+n%10*1000
funcs = [d,s,l,r]

name_dict = {d: "D", s: "S", l: "L", r: "R"}

def BFS(A, B):
    q = deque([(A, "")])

    while q:
        now, f = q.popleft()

        for func in funcs:
            next = func(now)
            next_f = f + name_dict[func]
            if not visited[next]:
                visited[next]=1
                if next == B:
                    return next_f
                q.append((next, next_f))


if __name__ == "__main__":
    T = int(rd())

    for _ in range(T):
        A, B = map(int, rd().split())
        visited = [0 for _ in range(10000)]
        ans = BFS(A, B)
        print(ans)
# git commit -m "code: Solve boj 09019 DSLR (yoonbaek)"