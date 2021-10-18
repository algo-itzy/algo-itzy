def solution(new_id):
    new_id = new_id.lower()  # 1단계

    res = ''  # 2단계
    for x in new_id:
        if x.isalnum() or x in '-_.':
            res += x

    while '..' in res:  # 3단계
        res = res.replace('..', '.')  

    if res[0] == '.' and len(res) > 1:  # 4단계
        res = res[1:]
    if res[-1] == '.':
        res = res[:-1]

    if not res:  # 5단계
        res = 'a'

    if len(res) >= 16:  # 6단계
        res = res[:15]

        if res[-1] == '.':
            res = res[:-1]

    if len(res) <= 3:  # 7단계
        res = res + res[-1] * (3-len(res))

    return res