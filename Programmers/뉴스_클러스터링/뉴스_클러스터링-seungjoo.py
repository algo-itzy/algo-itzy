# git commit -m "code: Solve programmers 뉴스 클러스터링 (seungjoo)"
def make_set(s):
    a = set()
    for i in range(len(s) - 1):
        if not s[i].isalpha() or not s[i+1].isalpha():
            continue
        now = s[i:i+2]
        while now in a:
            now += '1'
        a.add(now)
    return a

def solution(str1, str2):
    str1, str2 = str1.lower(), str2.lower()
    a = make_set(str1)
    b = make_set(str2)
    if not a | b:
        return 65536
    return len(a & b) * 65536 // len(a | b)