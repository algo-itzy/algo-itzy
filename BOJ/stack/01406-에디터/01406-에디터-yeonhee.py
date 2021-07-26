"""
처음에 풀이 1과 같이 풀었는데 시간 초과가 해결되지 않았습니다.
아마 pop(index) 때문인 것 같아서 index를 넣지 않기 위해 풀이 2에
7월 26일 수업시간에 (잠깐) 배운 collections.deque를 활용해봤습니다.
"""

# 풀이 1
"""
import sys
input = sys.stdin.readline

string = list(input().rstrip())        # input : 문자열의 한글자 한글자를 list의 요소로 받음 (\n을 제거하기 위한 rstrip)
cursor = len(string)                   # 커서는 문장의 맨 뒤에 위치

for _ in range(int(input())):          # input : 명령어의 개수
    cmd = input().split()              # input : 명령어를 list로 받음

    if cmd[0] == 'L':                  # L : 커서를 왼쪽으로 한 칸 옮김
        if cursor > 0:                 # 커서가 문장의 맨 앞이면 무시됨
            cursor -= 1
    elif cmd[0] == 'D':                # D : 커서를 오른쪽으로 한 칸 옮김
        if cursor < len(string):       # 커서가 문장의 맨 뒤이면 무시됨
            cursor += 1
    elif cmd[0] == 'B':                # B : 커서 왼쪽에 있는 문자를 삭제함
        if cursor != 0:                # 커서가 문장의 맨 앞이면 무시됨
            string.pop(cursor - 1)
            cursor -= 1                # 커서가 한 칸 왼쪽으로 이동 (여기서 정의한 커서는 절대적 위치이므로)
    elif cmd[0] == 'P':                # P : 문자열을 커서 왼쪽에 추가함
        string.insert(cursor, cmd[1])
        cursor += 1                    # 커서가 한 칸 오른쪽으로 이동

print(''.join(string))                 # 리스트를 string으로 변환하여 출력
"""

# 풀이 2
import sys
from collections import deque

input = sys.stdin.readline

# 커서 왼쪽은 left, 오른쪽은 right
left = deque(input().rstrip())          # input : 문자열의 한글자 한글자를 list의 요소로 받음 (\n을 제거하기 위한 rstrip)
right = deque()

for _ in range(int(input())):          # input : 명령어의 개수
    cmd = input().split()              # input : 명령어를 list로 받음

    if cmd[0] == 'L' and left:         # L : 커서를 왼쪽으로 한 칸 옮김 (커서가 문장의 맨 앞이면 무시됨)
        right.appendleft(left.pop())
    elif cmd[0] == 'D' and right:      # D : 커서를 오른쪽으로 한 칸 옮김 (커서가 문장의 맨 뒤이면 무시됨)
        left.append(right.popleft())
    elif cmd[0] == 'B' and left:       # B : 커서 왼쪽에 있는 문자를 삭제함 (커서가 문장의 맨 앞이면 무시됨)
        left.pop()
    elif cmd[0] == 'P':                # P : 문자열을 커서 왼쪽에 추가함
        left.append(cmd[1])

print(''.join(left + right))           # deque를 string으로 변환하여 출력