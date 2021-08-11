# solved by YoonBaek
# DFS / BFS 연습
import sys
from collections import deque

rd = sys.stdin.readline

class Stack:
    def __init__(self, items = []):
        self.items = items
        self.size = len(items)

    def push(self, x):
        self.items.append(x)
        self.size += 1
    
    def pop(self):
        stack.size -= 1
        return self.items.pop()

    def top(self):
        return self.items[-1]


# 76ms
def dfs(v: int):
    visited[v] = 1

    for i in graph[v]:
        if not visited[i]:
            dfs(i)


# 72ms
def dfs2(v: int):
    stack.push(v)

    while stack.size:
        now = stack.pop()

        for i in graph[now]:
            if not visited[i]:
                visited[i] = 1
                stack.push(i)
        
        
# 88ms
def bfs(v: int):
    queue.append(v)
    
    while queue:
        q_now = queue.popleft()

        for i in graph[q_now]:
            if not visited[i]:
                visited[i] = 1
                queue.append(i)


if __name__ == "__main__":
    n_nodes = int(rd().rstrip())
    n_paths = int(rd().rstrip())

    graph = [[] for _ in range(n_nodes+1)]
    visited = [0] * (n_nodes+1)
    stack = Stack()
    queue = deque()

    for _ in range(n_paths):
        start, end = map(int, rd().split())
        graph[start].append(end)
        graph[end].append(start)
    
    # dfs(1)
    # dfs2(1)
    bfs(1)
    print(sum(visited)-1)