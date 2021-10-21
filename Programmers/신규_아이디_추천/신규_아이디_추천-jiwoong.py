# git commit -m "code: Solve programmers 신규 아이디 추천 (jiwoong)"
def solution(idx):
    ans = ''
    idx = idx.lower()
    tmp = False
    for c in idx:
        if c.islower() or c.isdigit() or c == '-' or c == '_' or c == '.':
            if c == '.' and tmp == True:
                pass
            else:
                ans += c
                tmp = False
            if c == '.':
                tmp = True

    if len(ans) >= 1:
        if ans[0] == '.':
            ans = ans[1:]
    if len(ans) >= 1:
        if ans[-1] == '.':
            ans = ans[:-1]

    if len(ans) == 0:
        ans += 'a'

    if len(ans) >= 16:
        ans = ans[:15]
        if len(ans) >= 1:
            if ans[0] == '.':
                ans = ans[1:]
        if len(ans) >= 1:
            if ans[-1] == '.':
                ans = ans[:-1]

    if len(ans) <= 2:
        while len(ans) < 3:
            ans += ans[-1]

    return ans
