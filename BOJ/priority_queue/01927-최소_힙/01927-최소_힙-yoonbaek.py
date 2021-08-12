# solved by YoonBaek
import sys

rd = sys.stdin.readline
wr = sys.stdout.write

class MinHeap:
    def __init__(self):
        self.queue = []

    def push(self, n):
        self.queue.append(n)
        last_index = len(self.queue) - 1

        while 0 <= last_index:
            parent_index = self.parent(last_index)

            if 0 <= parent_index and self.queue[parent_index] > self.queue[last_index]:
                self.swap(last_index, parent_index)
                last_index = parent_index
            else:
                break

    def pop(self):
        last_index = len(self.queue)-1
        if last_index < 0:
            return 0

        self.swap(0, last_index)
        min_val = self.queue.pop()
        self.minHeapify(0)
        print("!!!", min_val)
        return min_val

    def parent(self, index):
        return (index-1) // 2

    def swap(self, i, parent_index):
        self.queue[i], self.queue[parent_index] = self.queue[parent_index], self.queue[i]

    def minHeapify(self, i):
        left_index = self.leftchild(i)
        right_index = self.rightchild(i)

        min_index = i
        if left_index >=len(self.queue)-1 and self.queue[min_index] > self.queue[left_index]:
            min_index = left_index
        if right_index >=len(self.queue)-1 and self.queue[min_index] > self.queue[right_index]:
            min_index = right_index

        # if not min
        if min_index != i:
            self.swap(i, min_index)
            self.minHeapify(min_index)

    def leftchild(self, index):
        return index*2 + 1

    def rightchild(self, index):
        return index*2 + 2

if __name__ == "__main__":
    mh = MinHeap()
    N = int(rd().rstrip())

    for _ in range(N):
        cmd = int(rd().rstrip())

        if cmd == 0:
            wr(f"{mh.pop()}\n")

        else:
            mh.push(cmd)



