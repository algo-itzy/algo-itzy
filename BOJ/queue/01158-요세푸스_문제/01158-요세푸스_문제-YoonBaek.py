# solved by YoonBaek
from sys import stdin

class Queue :

    def __init__(self, item, n):
        self.item = item
        self.size = n
    
    def push(self, x):
        self.size += 1
        self.item.append(x)

    def pop(self, idx):
        self.size -= 1
        pop = self.item.pop(idx)
        return pop

def solve():
    """
    python으로는 queue 전부 돌면서
    push pop 반복하면 시간 초과나서
    pop으로 idx 콕 찝어내는 방법을 고민했습니다.
    """
    result = "<"

    idx = k - 1
    while True :
        result += q.pop(idx) + ", "
        if not q.size:
            break
        # idx calc
        # q.size가 idx 보다 작으면 나눈 몫(= 순회)으로 인덱스를 정해줍니다.
        idx = (idx + k - 1) % q.size

    # erase comma, space and close 괄호 
    return result[:-2] + ">"

if __name__ == "__main__":
    n, k = map(int, stdin.readline().split())

    items = [str(i+1) for i in range(n)]
    q = Queue(items, n)

    print(solve())