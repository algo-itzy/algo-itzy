# python 3.10.0 required.
from heapq import heappush as hpush
from heapq import heappop as hpop

def solution(n, pointer, cmds):
    left, right = [-i for i in range(pointer, -1, -1)], [i for i in range(pointer+1, n)] # maxheap, minheap
    stack = []

    for cmd in cmds:
        match cmd.split():
            case ["U", cnt]:
                for _ in range(int(cnt)):
                    hpush(right, -hpop(left))
            case ["D", cnt]:
                for _ in range(int(cnt)):
                    hpush(left, -hpop(right))
            case ["C"]:
                stack.append(-hpop(left))
                if right:
                    hpush(left, -hpop(right))
            case _:
                z = stack.pop()
                if z < -left[0]:
                    hpush(left, -z)
                    continue
                hpush(right, z)

    answer = ["O"] * n
    while stack:
        answer[stack.pop()] = "X"

    return ''.join(answer)

print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))

# git commit -m "code: Solve programmers 표 편집 (yoonbaek)"