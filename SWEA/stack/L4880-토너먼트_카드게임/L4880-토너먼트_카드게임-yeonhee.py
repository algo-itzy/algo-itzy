import sys
sys.stdin = open('input.txt')


def get_winner(p1, p2):  # players
    win_cases = [(2, 1), (3, 2), (1, 3)]
    lose_cases = [(1, 2), (2, 3), (3, 1)]

    # 카드 가위바위보 시 승자의 인덱스 반환
    if cards[p1] == cards[p2]: return p1
    elif (cards[p1], cards[p2]) in win_cases: return p1
    elif (cards[p1], cards[p2]) in lose_cases: return p2


def card_game(s, e):  # start, end
    if s == e:
        return s

    # 재귀를 통해 실질적인 카드 게임 진행
    w1 = card_game(s, (s+e)//2)
    w2 = card_game((s+e)//2 + 1, e)
    return get_winner(w1, w2)


for t in range(1, int(input())+1):
    n = int(input())
    cards = list(map(int, input().split()))
    result = card_game(0, n-1)
    print(f'#{t} {result+1}')  # 학생 번호가 1부터 시작
