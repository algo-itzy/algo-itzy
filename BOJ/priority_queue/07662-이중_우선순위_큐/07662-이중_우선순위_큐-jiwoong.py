# import heapq, sys
# input = sys.stdin.readline
# t = int(input())

# 1번 풀이
"""
for _ in range(t):
    heap = []
    for i in range(int(input())):
        op, n = map(str, input().strip().split())
        if op == 'I':
            heapq.heappush(heap, int(n))
        else:
            if len(heap) == 0:
                continue
            if n == '-1':
                heapq.heappop(heap)
            else:
                heap = heapq.nsmallest(len(heap) - 1, heap)
                heapq.heapify(heap)
    if heap:
        print(heapq.nlargest(1, heap)[0], heap[0])
    else:
        print('EMPTY')
"""


# 2번 풀이
"""
for _ in range(t):
    q = []
    k = int(input())

    for _ in range(k):
        func, num = map(str, input().strip().split(' '))

        if func == 'I':
            heapq.heappush(q, int(num))
        else:
            if q:
                if num == '-1':
                    heapq.heappop(q)
                else:
                    q = heapq.nlargest(len(q), q)[1:]
                    heapq.heapify(q)

    if len(q) == 0:
        print('EMPTY')
    else:
        tmp = q[0]
        print(heapq.nlargest(1, q)[0], tmp)
"""

# 3번 풀이
"""
def que(q):
    tmp = []
    while q:
        heapq.heappush(tmp, -(heapq.heappop(q)))
    return tmp


for _ in range(t):
    q = []
    ascend = True
    k = int(input())
    for _ in range(k):
        func, num = map(str, input().strip().split(' '))
        if func == 'I':
            if ascend:
                heapq.heappush(q, int(num))
            else:
                heapq.heappush(q, -int(num))
        else:
            if q:
                if num == '-1':
                    if ascend:
                        heapq.heappop(q)
                    else:
                        q = que(q)
                        heapq.heappop(q)
                        ascend = True
                else:
                    if ascend:
                        q = que(q)
                        heapq.heappop(q)
                        ascend = False
                    else:
                        heapq.heappop(q)

    if len(q) == 0:
        print('EMPTY')
    else:
        if ascend:
            tmp = q[0]
            q = que(q)
            print(-q[0], tmp)
        else:
            tmp = -q[0]
            q = que(q)
            print(tmp, q[0])
"""

