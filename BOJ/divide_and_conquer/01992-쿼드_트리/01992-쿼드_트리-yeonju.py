n = int(input())

arr = [list(map(int, input())) for _ in range(n)]

result = []

def solution(x, y, n):
    global result
    color = arr[x][y]
    
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != arr[i][j]:  # 순서를 지키는 것이 중요 (왼위, 오위, 왼아, 오아)
                                    # 범위 안에 다른 값이 있으면 괄호 쳐주고 4등분
                result.append('(')
                solution(x,y,n//2)
                solution(x,y+n//2, n//2)
                solution(x+n//2, y, n//2)
                solution(x+n//2, y+n//2, n//2)
                result.append(')')
                return
    result.append(color)

solution(0,0,n)
print("".join(map(str,(result))))
            



# git commit -m "code: Solve boj 01992 쿼드 트리 (yeonju)"