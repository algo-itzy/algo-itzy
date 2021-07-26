import sys

# 테스트 개수 입력
test_num = int(input())

for _ in range(test_num):
    # 스택 구조를 활용할 리스트 선언
    stacks = []
    # test 결과를 저장할 bool 변수 생성
    flag = True
    vps_list = sys.stdin.readline()
    for word in vps_list:
        # 왼쪽 괄호 입력받으면 계속 스택에 추가
        if word == '(':
            stacks.append(1)
        # 오른쪽 괄호는 왼쪽 괄호와 만나 하나의 쌍을 이루므로 pop의 형태로 생각할 수 있음   
        elif word == ')':
            # 스택이 비어있는데 오른쪽 괄호가 오면 pop을 할 수 없으므로 false, 바로 break
            if len(stacks) == 0:
                flag = False
                break
            else:
                stacks.pop()

    # 저장된 테스트 결과에 따라 출력, stack이 비어있어야 true          
    if flag == True and len(stacks) == 0:
        print('YES')
    else:
        print('NO')