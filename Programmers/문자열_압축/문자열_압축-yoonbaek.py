def solution(s):
    answer = len(s)
    len_ = len(s)

    res = ''
    mul = 1
    for i in range(1, len_//2+1):
        prev = ''
        for n in range(0, len_//i+1):
            cur = s[i*n:i*(n+1)]
            if prev == cur:
                mul += 1
            if prev != cur:
                if mul != 1:
                    word = str(mul) + prev
                else:
                    word = prev
                res += word
                mul  = 1
            prev = cur
        
        res += prev
        answer = min(answer, len(res))
        res = ''
            
    return answer

# git commit -m "code: Solve programmers 문자열 압축 (yoonbaek)"