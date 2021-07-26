"""
문제가 이해가 되지 않아서..ㅠㅠ 접근 방법을 아래 링크에서 참고했습니다.
https://st-lab.tistory.com/182
"""

import sys
input = sys.stdin.readline

stack = []                     # 임시 리스트 (스택)
operators = []                 # 결과로 출력할 연산자
cnt = 1                        # key number
is_possible = True             # 불가능한 경우 체크

for _ in range(int(input())):  # 테스트 케이스 개수
    number = int(input())      # 수열을 이루는 정수 : 입력값

    while cnt <= number:       # 입력값보다 key number가 작을 경우, stack에 쌓는 과정
        stack.append(cnt)
        operators.append('+')
        cnt += 1
    
    if stack.pop() == number:  # stack에서 입력값을 추출하는 과정 (pop)
        operators.append('-')
    else:
        is_possible = False    # stack에서 입력값이 추출되지 않을 경우 반복문 종료
        break

print('NO' if not is_possible else '\n'.join(operators))