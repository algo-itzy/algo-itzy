def get_set(word: list):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    alpha = set(alpha)

    res, prev = set(), ''

    for char in word:
        if prev:
            cnt = 0
            target = prev+char
            if target.isalpha():
                while (cnt, target) in res:
                    cnt += 1
                res.add((cnt, target))
        prev = char
    
    return res

def solution(str1: str, str2: str):
    answer = 65536
    str1, str2 = str1.lower(), str2.lower()

    setA, setB = get_set(str1), get_set(str2)
    if setA or setB:
        answer = int(65536 * len(setA.intersection(setB)) / len(setA.union(setB)))

    return answer

# git commit -m "code: Solve programmers 뉴스 클러스터링 (yoonbaek)"