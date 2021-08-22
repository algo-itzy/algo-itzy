B_WIN = ((1, 2), (2, 3), (3, 1))  # B가 이기는 경우

def game(s, e):
    if s == e:  # 부전승
        return s

    w1 = game(s, (s+e)//2)
    w2 = game((s+e)//2 + 1, e)

    return w2 if (card[w1], card[w2]) in B_WIN else w1

for tc in range(1, int(input())+1):
    N = int(input())
    card = [0] + list(map(int, input().split()))

    print(f'#{tc}', game(1, N))

# 와.. 문제 가독성 보고 현타가 옵니다. 토너먼트 방식이 아닌가? 왤케 말을 어렵게 하지