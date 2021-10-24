def solution(p):
    if not p:
        return p
    
    cnt, i = 0, 0
    for c in p:
        i += 1
        if c == "(":
            cnt+=1
        else:
            cnt-=1
        if cnt == 0:
            break
    
    u, v = p[:i], p[i:]
    s = []

    for c in u:
        if c == "(":
            s.append(c)
        else:
            if s:
                s.pop()
            else:
                u = u[1:-1]
                word = ""
                for c in u:
                    if c == "(":
                        word += ")"
                    else:
                        word += "("
                return "(" + solution(v) + ")" + word

    return u + solution(v)