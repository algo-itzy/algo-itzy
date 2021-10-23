def solution(s):
    res = len(s)  # max 초기화
    
    for i in range(1, len(s)//2  + 1):
        tmp = ""
        cnt = 1
        x = s[:i]

        for j in range(i, len(s), i):
            if s[j : j+i] == x:
                cnt += 1
            else:  # 반복 끊길 때
                cnt = cnt if cnt > 1 else ""
                tmp += str(cnt) + x
                x = s[j : j+i]
                cnt = 1

        cnt = cnt if cnt > 1 else ""
        tmp += str(cnt) + x

        # tmp = tmp.replace('1', '')
        res = min(res, len(tmp))

    return res

# 반복 횟수가 10 이상일 때 예외처리 때문에 replace 못써요...