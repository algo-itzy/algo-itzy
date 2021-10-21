def solution(new_id):
    id = ''
    # 1
    new_id = new_id.lower()

    # 2
    for i in new_id:
        if i.isalpha() or i.isdigit() or i in ['-', '_', '.']:
            id += i

    # 3
    while '..' in id:
        id = id.replace('..', '.')

    # 4
    if id[0] == '.' and len(id) > 2: # 여기서 id 의 길이가 2보다 크다는 조건을 안 주면, 에러
        id = id[1:]
    if id[-1] == '.':
        id = id[:-1]

    # 5
    if id == '':
        id = 'a'

    # 6
    if len(id) > 15:
        id = id[:15]
    if id[-1] == '.':
        id = id[:-1]

    # 7
    while len(id) < 3:
        id += id[-1]

    return id


# git commit -m "code: Solve programmers 신규 아이디 추천 (yeonju)"