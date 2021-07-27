import sys 

left_stack = list(sys.stdin.readline()[:-1]) # 커서를 역순으로 만들기
right_stack = list() 
testcase = int(sys.stdin.readline()) # 입력할 명령어의 갯수가 입력됨

for i in range(testcase): 
    cmd = sys.stdin.readline()
     if cmd[0] == 'L' and left_stack : # 커서 왼쪽으로 한 칸 옮기기
         right_stack.append(left_stack.pop()) 
    elif cmd[0] == 'D' and right_stack : # 커서를 오른쪽으로 한 칸 옮기기
        left_stack.append(right_stack.pop()) 
    elif cmd[0] == 'B' and left_stack : # 커서 왼쪽 문자를 삭제
        left_stack.pop() 
    elif cmd[0] == 'P': left_stack.append(cmd[1]) #커서 왼쪽에 문자 추가

sys.stdout.write(''.join(left_stack + right_stack[::-1]))
