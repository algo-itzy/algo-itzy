import sys
import math
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T+1):
    
    words = input()
    stack = []

    for word in words:
        if not stack:  # 비어 있으면 추가
            stack.append(word)
        else:
            if stack[-1] == word:  # 스택 마지막 문자와 같으면 pop
                stack.pop()
            else:
                stack.append(word)  # 스택 마지막 문자와 다르면 append
    
    print(f'#{test_case} {len(stack)}')