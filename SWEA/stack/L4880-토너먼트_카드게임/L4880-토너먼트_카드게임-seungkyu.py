import sys
sys.stdin = open('input.txt')

def battle(start, end):
    
    if start == end:  # 대결 상대 없으므로 이긴 것으로 치고 return
        return start

    a = battle(start, (start+end)//2)
    b = battle((start+end)//2 + 1, end)

    if (numbers[a] == 1 and numbers[b] == 2) or (numbers[a] == 2 and numbers[b] == 3) or (numbers[a] == 3 and numbers[b] == 1):
        return b
    else:
        return a


T = int(input())

for test_case in range(1, T+1):

    N = int(input())
    # 인덱스가 사람 이름(번호)가 되도록 설정
    numbers = [0] + list(map(int, input().split()))

    print(f'#{test_case} {battle(1, N)}')
