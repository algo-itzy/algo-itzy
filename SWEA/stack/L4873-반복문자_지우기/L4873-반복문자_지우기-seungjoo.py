
def repeat_str(s):
    init = len(s)
    stack = []
    cnt = 0
    while s:
        pre = s.pop()
        if stack:
            if pre == stack[-1]:
                stack.pop()
                cnt += 1
            else:
                stack.append(pre)
        else:
            stack.append(pre)
    return init - 2*cnt


for test in range(1,int(input())+1):
    s = list(input())
    print(f'#{test} {repeat_str(s)}')