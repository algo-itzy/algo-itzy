# solved by Yoon Baek
from sys import stdin

# 큐 푼거 베꼈어용

class Deque :
    """
    구현하래서 구현하는 덱
    """

    def __init__(self, item, n = 0):
        self.item = item
        self.size = n
    
    def push_back(self, x):
        self.size += 1
        self.item.append(x)

    def push_front(self, x):
        self.size += 1
        self.item = [x]+self.item

    def pop_front(self):
        if self.size:
            self.size -= 1
            pop = self.item.pop(0)
        else:
            return -1
        return pop

    def pop_back(self):
        if self.size:
            self.size -= 1
            pop = self.item.pop()
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

    if cmd[0] == "push_front":
        d.push_front(cmd[1])
    if cmd[0] == "push_back":
        d.push_back(cmd[1])
    if cmd[0] == "pop_front":
        print(d.pop_front())
    if cmd[0] == "pop_back":
        print(d.pop_back())
    if cmd[0] == "size":
        print(d.size)
    if cmd[0] == "empty":
        print(d.empty())
    if cmd[0] == "front":
        print(d.front())
    if cmd[0] == "back":
        print(d.back())

if __name__ == "__main__":
    inputs = stdin.read().rstrip().split("\n")

    d = Deque([])
    
    for cmd in inputs[1:]:
        solve(cmd)
