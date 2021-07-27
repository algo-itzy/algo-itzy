# solved by YoonBaek
import sys

class Stack :
    item = []

    def push(self, x) :
        self.item.append(x)

    def pop(self) :
        pop = self.item[-1]
        self.item = self.item[:-1]
        return pop

    def top(self) :
        return self.item[-1]

def get_stack_elem():
    return int(sys.stdin.readline())

def solve():
    # 1 부터 시작하는 등차수열 원소
    sq_elem = 1

    for pop in pops :
        # 등차수열에서 pop 된 원소들과 등차수열 비교 후 append 지속
        while sq_elem <= pop:
            stack.push(sq_elem) 
            ops.append("+")
            sq_elem += 1
        
        # 같아질 때 pop
        if stack.top() == pop :
            stack.pop()
            ops.append("-")

        else :
            # No 출력 후 종료
            print("NO")
            return
    print(*ops, sep = '\n')

if __name__ == '__main__':
    n = int(input())

    stack = Stack()
    stack.item=[]
    ops = []
    # input으로 들어오는 pop들
    pops = []

    for _ in range(n):
        pops.append(get_stack_elem())

    solve()

        
        

