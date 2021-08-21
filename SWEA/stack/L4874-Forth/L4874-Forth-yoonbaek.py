# solved by YoonBaek
from collections import deque


class OperationError:
    """
    연산자가 더 많거나, 연산자 없이 홀로 있는 값이 있을 때 예외가 발생합니다.
    실제로 exception을 받게 되면 프로그램이 끝나기 때문에 받지 않았습니다.
    """
    def __init__(self, tc):
        self.tc = tc
    
    def __str__(self):
        return f"#{self.tc} error"


def compute(right, left: str, operator: str):
    if operator == "/":
        operator *= 2
    return str(eval(left+operator+right))


if __name__ == "__main__":
    T = int(input())

    for tc in range(1, T+1):
        nums_and_ops = input().split()

        stack = deque()

        for num_or_op in nums_and_ops:

            if num_or_op.isdigit():
                stack.append(num_or_op)

            elif num_or_op == ".":
                if len(stack) > 1:
                    print(OperationError(tc))
                else: 
                    print(f"#{tc}", "".join(stack))
            
            else:
                if len(stack) < 2:
                    print(OperationError(tc))
                    break
                else:
                    right, left = stack.pop(), stack.pop()
                    c = compute(left, right, num_or_op)
                    stack.append(c)