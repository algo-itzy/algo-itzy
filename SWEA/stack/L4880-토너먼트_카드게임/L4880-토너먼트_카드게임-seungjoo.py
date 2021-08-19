
def rock_siccor_paper(fights):
    length = len(fights)
    if length==1:
        return fights[0]
    elif length==2:
        if fights[0][1]==1:
            if fights[1][1]==1 or fights[1][1]==3:
                return fights[0]
            elif fights[1][1]==2:
                return fights[1]
        elif fights[0][1]==2:
            if fights[1][1]==1 or fights[1][1]==2:
                return fights[0]
            elif fights[1][1]==3:
                return fights[1]
        else:
            if fights[1][1]==2 or fights[1][1]==3:
                return fights[0]
            elif fights[1][1]==1:
                return fights[1]
    else:
        return rock_siccor_paper([rock_siccor_paper(fights[:(length+1)//2]),rock_siccor_paper(fights[(length+1)//2:])])



for test in range(1,int(input())+1):
    N = int(input())
    cards = list(map(int, input().split()))
    cards_idx = [[idx+1,cards] for idx, cards in enumerate(cards)]
    # 1가위, 2 바위 3 보
    winner, number = rock_siccor_paper(cards_idx)
    print(f'#{test} {winner}')