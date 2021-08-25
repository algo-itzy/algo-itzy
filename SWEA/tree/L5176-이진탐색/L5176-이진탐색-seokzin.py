def inorder(n):
    global cnt

    if n <= N:
        inorder(n*2)      # left

        arr[n] = cnt      # root
        cnt += 1             

        inorder(n*2 + 1)  # right


for tc in range(1, int(input())+1):
    N = int(input())
    arr = [0 for _ in range(N+1)]
    cnt = 1

    inorder(1)  # 1부터 넣기 시작

    print(f'#{tc}', arr[1], arr[N//2])

# 생소한 문제라 어려웠습니다. 코드 참조했음
# cnt를 글로벌하게 관리하는게 핵심인듯