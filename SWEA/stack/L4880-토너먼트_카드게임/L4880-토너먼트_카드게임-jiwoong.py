# 분할 정복
def DCA(tournament):
    # 올라올 때마다 2명씩
    if len(tournament) == 2:

        # 가위 바위 보
        if tournament[0][0] == "1":
            if tournament[1][0] == "1" or tournament[1][0] == "3":
                return "1", tournament[0][1]
            else:
                return "2", tournament[1][1]

        elif tournament[0][0] == "2":
            if tournament[1][0] == "2" or tournament[1][0] == "1":
                return "2", tournament[0][1]
            else:
                return "3", tournament[1][1]

        else:
            if tournament[1][0] == "3" or tournament[1][0] == "2":
                return "3", tournament[0][1]
            else:
                return "1", tournament[1][1]

    # 한 명일 때
    elif len(tournament) == 1:
        return tournament[0][0], tournament[0][1]

    # 2명 이상일 떄
    else:
        num = len(tournament)
        # Divide and Conquer
        return DCA([DCA(tournament[:num // 2 + num % 2]), DCA(tournament[num // 2 + num % 2:])])


if __name__ == "__main__":
    T = int(input())
    for tc in range(1, T + 1):
        N = int(input())
        cards = input().split()

        students = [i + 1 for i in range(N)]

        ans = DCA(list(zip(cards, students)))

        print("#{} {}".format(tc, ans[1]))
