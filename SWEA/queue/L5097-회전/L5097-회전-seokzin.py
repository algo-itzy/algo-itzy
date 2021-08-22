for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    print(f'#{tc}', input().split()[m%n])

# 문제 의도가 뭘까요.. 일부러 pop()을 썼어야 했나?