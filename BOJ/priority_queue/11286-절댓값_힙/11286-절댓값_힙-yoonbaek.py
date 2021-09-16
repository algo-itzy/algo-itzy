from sys import stdin
import heapq

rd = lambda : int(stdin.readline())

min_heap = []

if __name__ == "__main__":
    N = rd()
    for _ in range(N):
        x = rd()

        if x:            
            heapq.heappush(min_heap, (abs(x), x))
        else:
            if not min_heap:
                print(0)
                continue
            print(heapq.heappop(min_heap)[1])

# git commit -m "code: Solve boj 11286 절댓값 힙 (yoonbaek)"