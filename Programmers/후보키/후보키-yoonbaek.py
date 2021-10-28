def combination(visited, r, comb, N):
    global combs

    if len(comb) == r:
        combs.append(tuple(comb))
        return

    start = 0 if not comb else comb[-1]
    for i in range(start , N):
        if not visited[i]:
            visited[i] = 1
            combination(visited, r, comb + [i], N)
            visited[i] = 0  


def solution(relations):
    global combs
    N = len(relations[0])
    visited = [0] * N
    table, candidates = set(), set()


    combs = []
    # 후보키 조합 구하기
    for i in range(1, N+1):
        combination(visited, i, [], N)
    
    # 후보 키 조합 중 유일성 만족 키 식별
    for comb in combs:
        for relation in relations:
            key = ""
            for c in comb:
                # 열 내부 데이터간 중복을 str(c) cat을 통해 필터링
                key += str(c)+relation[c]
            if key in table:
                break
            else:
                table.add(key)
        else:
            candidates.add(comb)

    # 후보 키 조합 중 최소성 만족 키 식별
    pop_set = set()
    for key in candidates:
        for second_key in candidates:
            if key != second_key and set(key).issubset(set(second_key)):
                pop_set.add(second_key)

    for key in pop_set:
        candidates.remove(key)
        candidates.pop(key)
    
    return len(candidates)

# git commit -m "code: Solve programmers 후보키 (yoonbaek)"