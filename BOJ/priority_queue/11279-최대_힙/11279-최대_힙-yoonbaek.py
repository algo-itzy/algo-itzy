# git commit -m "Solve boj 11279 최대 힙 (yoonbaek)"
# 0이면 pop
# 자연수면 push
import sys

input = lambda : int(sys.stdin.readline())
output = sys.stdout.write

class MaxHeap:
    def __init__(self):
        self.queue = []

    def push(self, n):
        self.queue.append(n)
        last_index = len(self.queue) - 1

        while 0 <= last_index:
            parent_index = self.parent(last_index)

            if 0 <= parent_index and self.queue[parent_index] < self.queue[last_index]:
                self.swap(last_index, parent_index)
                last_index = parent_index
            else:
                break

    def pop(self):
        last_index = len(self.queue)-1
        # if empty
        if last_index < 0:
            return 0

        self.swap(0, last_index)
        max_val = self.queue.pop()
        self.maxHeapify(0)

        return max_val

    def swap(self, i, parent_index):
        self.queue[i], self.queue[parent_index] = self.queue[parent_index], self.queue[i]

    def maxHeapify(self, i):
        left_index = self.leftchild(i)
        right_index = self.rightchild(i)

        max_index = i
        if left_index <= len(self.queue)-1 and self.queue[max_index] < self.queue[left_index]:
            max_index = left_index
        if right_index <= len(self.queue)-1 and self.queue[max_index] < self.queue[right_index]:
            max_index = right_index

        # if not max
        if max_index != i:
            self.swap(i, max_index)
            self.maxHeapify(max_index)

    # 배열 상에서 트리 상위 노드 인덱스
    def parent(self, index):
        return (index-1) // 2
    # 배열 상에서 왼쪽 자식
    def leftchild(self, index):
        return index*2 + 1
    # 배열 상에서 오른쪽 자식
    def rightchild(self, index):
        return index*2 + 2

if __name__ == "__main__":
    N = input()
    max_heap = MaxHeap()

    for _ in range(N):
        cmd = input()

        if cmd:
            max_heap.push(cmd)
        else:
            output(f"{max_heap.pop()}\n")