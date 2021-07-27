import sys

class Editor :
    item = []

    def size(self):
        return len(self.item)
    
    def pop(self) :
        if self.size() > 0:
            # this is slow
            # pop = self.item[-1]
            # self.item = self.item[:-1]
            pop = self.item.pop()
            return pop

    def push(self, x) :
        self.item.append(x)

def solve(left, right, cmd) :

    cmd = cmd.split()

    if cmd[0] == "L":
        move = left.pop()
        if move is not None:
            right.push(move)

    if cmd[0] == "D":
        move = right.pop()
        if move is not None:
            left.push(move)

    if cmd[0] == "B":
        left.pop()

    if cmd[0] == "P":
        left.push(cmd[1])

if __name__ == "__main__" :
    cmds = sys.stdin.read().rstrip().split("\n")
    word = cmds[0]
    cmds = cmds[2:]

    left, right = Editor(), Editor()
    left.item = list(word)

    for cmd in cmds :
        solve(left, right, cmd)

    print("".join(left.item + right.item[::-1]))