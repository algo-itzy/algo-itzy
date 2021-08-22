import sys
sys.stdin = open('sample_input.txt')

def calculate(operation):
    stack = []
    ans = 0
    try:
        for chr in operation:
            if chr.isdigit():  # 숫자일 때 append
                stack.append(int(chr))
            elif chr == '.':  # . 나오면 stack에 저장된 값 pop
                ans = stack.pop()
                break
            else:
                a = stack.pop()
                b = stack.pop()
                if chr == '+':
                    ans = b+a
                elif chr == '-':
                    ans = b-a
                elif chr == '*':
                    ans = b*a
                elif chr == '/':
                    ans = b//a
                stack.append(ans)
    except:  # stack pop할 때 원소 부족하면 오류
        return 'error'

    if len(stack) >= 1:  # ans pop했는데도 값 남아있으면 오류
        return 'error'
    else:
        return ans

T = int(input())

for test_case in range(1, T+1):
    operation = input().split()
    print(f'#{test_case} {calculate(operation)}')
    