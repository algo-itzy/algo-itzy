def solution(p):
    if not p:
        return p

    u = ''
    v = ''

    # 균형잡힌 괄호 문자열 분리
    for idx in range(2, len(p)+1, 2):
        if p[:idx].count("(") == p[:idx].count(")"):
            u = p[:idx]
            v = p[idx:]
            break

    # u가 올바른 괄호 문자열이라면 v에 대해 수행
    if u[0] == "(" and u[-1] == ")":
        u += solution(v)
        return u

    else:  # 4번 과정 수행
        result = ''
        result += "(" + solution(v) + ")"
        k = u[1:-1]
        a = ''
        for i in k:
            result += ")" if i == "(" else "("
        return result
