"""
# 괄호검사
괄호 {}, ()가 제대로 짝을 이뤘는지 검사
정상적으로 짝을 이룬 경우 1, 그렇지 않으면 0을 출력

첫 줄에 테스트 케이스 개수 T가 주어진다.
다음 줄부터 테스트 케이스 별로 온전한 형태이거나 괄호만 남긴 한 줄의 코드가 주어진다.

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력
"""

T = int(input())

for tc in range(1, T+1):
    words = input()
    stack = []
    ans = 1
    for word in words:
        # 괄호 아니면 넘어가기
        if word not in ('(', ')', '{', '}'):
            continue
        else:
            # (면 삽입
            if word == '(' or word == '{':
                stack.append(word)
            # )면 종료
            elif word == ')':
                if len(stack) == 0:
                    ans = 0
                    break
                # pop 했을 때 (가 아니면 종료
                check = stack.pop()
                if check != '(':
                    ans = '0'
                    break
            else:
                if len(stack) == 0:
                    ans = 0
                    break
                check = stack.pop()
                if check != '{':
                    ans = 0
                    break
    # 반복문 종료 후 스택에 값이 남아있으면 종료
    else:
        if len(stack) != 0:
            ans = 0

    print(f"#{tc} {ans}")
