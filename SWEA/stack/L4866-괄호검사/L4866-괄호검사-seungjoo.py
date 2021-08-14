
def bracket_inspection(s):
    dic = {')':0, '}':0,']':0, '(':0, '{':0,'[':0}
    stack1 = []
    stack2 = []
    for chr in s:
        if chr in dic:
            dic[chr] += 1
            stack1.append(chr)

    if dic[')'] != dic['('] or dic['}'] != dic['{'] or dic[']'] != dic['[']:
        return 0

    while stack1:
        check = stack1.pop()
        if check == ')' or check == '}' or check==']':
            stack2.append(check)
        else:
            if check =='(':
                if stack2[-1]==')':
                    dic[stack2.pop()] -=1
                else:
                    return 0
            elif check=='{':
                if stack2[-1]=='}':
                    dic[stack2.pop()] -= 1
                else:
                    return 0
            elif check=='[':
                if stack2[-1]==']':
                    dic[stack2.pop()] -= 1
                else:
                    return 0
        
    return 1
        

for test in range(1,int(input())+1):
    s = list(input())
    print(f'#{test} {bracket_inspection(s)}')
