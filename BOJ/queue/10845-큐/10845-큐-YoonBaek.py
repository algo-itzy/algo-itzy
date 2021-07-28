# solved by Yoon Baek
from sys import stdin

# 구현하래서 구현하는 큐
class Queue :

    def __init__(self, item, n = 0):
        self.item = item
        self.size = n
    
    def push(self, x):
        self.size += 1
        self.item.append(x)

    def pop(self):
        if self.size:
            self.size -= 1
            pop = self.item.pop(0)
        else:
            return -1
        return pop

    def empty(self):
        if self.size:
            return 0
        return 1
    
    def front(self):
        if self.size:
            return self.item[0]
        return -1

    def back(self):
        if self.size:
            return self.item[-1]
        return -1

def solve(cmd):
    cmd = cmd.split()

    if cmd[0] == "push":
        q.push(cmd[1])
    if cmd[0] == "pop":
        print(q.pop())
    if cmd[0] == "size":
        print(q.size)
    if cmd[0] == "empty":
        print(q.empty())
    if cmd[0] == "front":
        print(q.front())
    if cmd[0] == "back":
        print(q.back())

if __name__ == "__main__":
    inputs = stdin.read().rstrip().split("\n")

    q = Queue([])
    
    for cmd in inputs[1:]:
        solve(cmd)
