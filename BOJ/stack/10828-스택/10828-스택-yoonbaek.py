# solved by YoonBaek
import sys

class Stack:
    '''
    stack class 정의
    '''
    item = []

    # stack 클래스 메서드 구성
    def push(self, x):
        self.item.append(x)

    def pop(self):
        if self.empty() :
            return -1
        return self.item.pop()

    def size(self):
        return len(self.item)

    def empty(self):
        return 0 if self.item else 1

    def top(self):
        if self.empty() :
            return -1
        else :
            return self.item[-1]

def solve() :
    s = Stack()
    cmd = sys.stdin.readline().split()

    if cmd[0] == "push":
        s.push(cmd[1])
    elif cmd[0] == "pop":
        print(s.pop())
    elif cmd[0] == "size":
        print(s.size())
    elif cmd[0] == "empty":
        print(s.empty())
    elif cmd[0] == "top":
        print(s.top())

if __name__ == '__main__':
    N = int(input())

    for _ in range(N):
        solve()