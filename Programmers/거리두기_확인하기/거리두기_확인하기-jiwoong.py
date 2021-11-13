# git commit -m "code: Solve programmers 거리두기 확인하기 (jiwoong)"
def solution(places):
    answer = []

    for p in places:
        check = True
        for i in range(5):
            for j in range(5):
                if p[i][j] == 'P':
                    if j + 1 < 5:
                        if p[i][j + 1] == 'P':
                            check = False
                            break
                        elif j + 2 < 5:
                            if p[i][j + 1] == 'O' and p[i][j + 2] == 'P':
                                check = False
                                break
                        if i + 1 < 5:
                            if (p[i][j + 1] == 'O' or p[i + 1][j] == 'O') and p[i + 1][j + 1] == 'P':
                                check = False
                                break
                    if i + 1 < 5:
                        if p[i + 1][j] == 'P':
                            check = False
                            break
                        elif i + 2 < 5:
                            if p[i + 1][j] == 'O' and p[i + 2][j] == 'P':
                                check = False
                                break
                        if j - 1 >= 0:
                            if (p[i][j - 1] == 'O' or p[i + 1][j] == 'O') and p[i + 1][j - 1] == 'P':
                                check = False
                                break
        if check:
            answer.append(1)
        else:
            answer.append(0)

    return answer
