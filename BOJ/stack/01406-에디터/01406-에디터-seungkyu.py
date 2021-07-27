# 시간 제한이 짧은 문제이므로 시간 복잡도를 최소화해야 함
# 처음 풀이 스택 사용 X => 계속 시간 초과
# 스택 2개 사용 (풀이 참고함)
import sys
left_stack = list(sys.stdin.readline().rstrip())
right_stack = []
# 커서 위치가 왼쪽 스택의 top부분과 오른쪽 스택의 top부분에 존재
# cursor_idx = len(left_stack)
m = int(input())
for _ in range(m):
    command = sys.stdin.readline().split()
    if command[0] == 'L':
        if left_stack:
            # 왼쪽에서 원소를 뽑아 오른쪽 스택으로 이동
            right_stack.append(left_stack.pop())
    elif command[0] == 'D':
        if right_stack:
            # 오른쪽에서 원소를 뽑아 왼쪽 스택으로 이동
            left_stack.append(right_stack.pop())
    elif command[0] == 'B':
        if left_stack:
            # del 사용 했더니 -> O(N) 계속 시간 초과
            # del word[]
            left_stack.pop()
    elif command[0] == 'P':
        input_word = command[1]
        # insert 사용 했더니 -> O(N) 계속 시간 초과
        # word.insert()
        left_stack.append(input_word)
# 오른쪽 스택은 원하는 순서에서 뒤집혀서 출력되므로 reversed 사용
print(''.join(left_stack + list(reversed(right_stack))))
