# . 이 나오면 stop
# . 이 나왔는 데에도 스택에 원소가 0이거나 2개 이상이면 error => 오직 스택의 원소만 1개만 있어야 함
# 연산 앞에 원소가 2개 미만이면 error 

t = int(input())

for tc in range(t):
    li = list(map(str, input().split()))    # 공백을 기준으로 값(정수, 연산자)을 입력 받음 

    stack = []                              # 숫자만 쌓을 스택 리스트 
    ans = 0                                 # 계산결과 변수 ans

    for i in li:
        if i == '.':                        # '.' 이 나오면 stop                    
            break


        if i.isdigit():                     # string 타입이 숫자인지 확인하는 함수 
            stack.append(int(i))            # 값이 숫자이면 스택에 추가

        else:                               # 값이 숫자가 아니고 연산이면
            
            if len(stack) >= 2:                            
           
                t1 = stack.pop()            # stack 의 마지막에 있는 2개의 함수를 pop 해서 연산을 해줌
                t2 = stack.pop()
                
                if i == '+':
                    stack.append(t1 +t2)
                elif i == '-':
                    stack.append(t2 - t1)
                elif i == '*':
                    stack.append(t1 * t2)
                else:
                    stack.append(t2 // t1)
            else: 
                ans = 'error'
       
              
          
    if len(stack) == 1 and ans != 'error' :            # 형식이 맞아 연산이 성공하면
        ans = stack.pop() 
    else:                           # 형식이 잘못되어 연산이 불가능한 경우
        ans = 'error'


    print(f'#{tc+1} {ans}')


        
