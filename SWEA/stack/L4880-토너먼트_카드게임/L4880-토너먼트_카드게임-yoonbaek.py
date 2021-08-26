# solved by YoonBaek


# rock paper scissors
def rps(l, r: int):
    if l == 1 and r == 2:
        return 0
    if l == 2 and r == 3:
        return 0
    if l == 3 and r == 1:
        return 0
    return 1
        

def game(l_idx, r_idx: int) -> int:
    return l_idx if rps(cards[l_idx], cards[r_idx]) else r_idx


def tournament(left, right: int):
    if left == right:
        return left

    mid = (left+right)//2
    
    game1 = tournament(left, mid)
    game2 = tournament(mid+1, right)

    return game(game1, game2)
    

if __name__ == "__main__":
    T = int(input())

    for tc in range(1, T+1):
        N = int(input())
        cards = list(map(int, input().split()))

        print(f"#{tc} {tournament(0, N-1)+1}")