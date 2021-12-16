# git commit -m "code: Solve boj 02263 트리의 순회 (seungkyu)"
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def preorder(in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end:
        return
    
    # 루트는 post에서 마지막 원소
    root = postorders[post_end]
    print(root, end=' ')
    pos = position[root]
    left = pos-in_start

    preorder(in_start, pos-1, post_start, post_start+left-1)
    preorder(pos+1, in_end, post_start+left, post_end-1)


n = int(input())
inorders = list(map(int, input().split()))
postorders = list(map(int, input().split()))
position = [0]*100001

# 시간 초과 안나도록 미리 찾아놓기
for i in range(n):
    position[inorders[i]] = i

preorder(0, n-1, 0, n-1)