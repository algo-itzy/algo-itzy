for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    w = sorted(list(map(int, input().split())))
    t = sorted(list(map(int, input().split())))
    res = 0
    
    for _ in range(min(n, m)):  # 최소 횟수로 해야 pop() = null 오류 없어짐 
        if t[-1] >= w[-1]:
            res += w[-1]
            t.pop()
        
        w.pop()

    print(f"#{tc}", res)

# 전형적 배낭 문제