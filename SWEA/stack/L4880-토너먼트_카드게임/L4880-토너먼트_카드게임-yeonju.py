# 푼다고 풀었는데, 에러가 발생해서 조금 더 들여다 보고 다시 제출하겠습니다 ㅠ-ㅠ

# 1 가위  < 2 바위 < 3 보 < 1 가위 
# 같은 카드이면 작은 번호가 승 
# 두 그룹이 각각 1명이 되면 카드 비교 -> 반복

def rockpaperscissors(a, b):                # 가위바위보 하는 함수 
    left, right = cards[a-1], cards[b-1]    # 1번 카드를 가진 학생의 인덱스 번호는 0이기에 -1 씩 해주기 

    if left == right:                       # 같은 카드면 작은 번호가 승 
        return left
   
    elif left == 1:                         # 가위
        if right == 3: 
            return left
        elif right == 2: 
            return right
    elif left == 2:                          # 바위
        if right == 1:
            return left
        elif right ==3:
            return right
    elif left == 3:                          # 보
        if right == 1:
            return right
        elif right == 2:
            return left

def game(i, j):                             # 인원이 1이 될 때까지 반으로 쪼개기
    if i == j:
        return i
    else: 
        mid = (i+j) // 2    
        k = game(i,mid)
        l = game(mid+1, j)
        return rockpaperscissors(k,l)

t = int(input())

for tc in range(t):
    n = int(input())
    cards = list(map(int, input().split()))   # n명이 고른 카드 번호순으로 입력 받기

    cards = enumerate(cards, start =1)

    print(f'#{tc+1} {game(1,n)}')             # 학생 번호는 1 ~  n 번까지

