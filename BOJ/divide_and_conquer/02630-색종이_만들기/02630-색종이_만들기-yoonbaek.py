# set으로 풀었는데 로직이 별로라 그렇게 빠르지는 않은 거 같습니다.
# 그냥 단순 순회로 다른 색 찾으면 break 하는 로직이 더 나을거 같습니다.

from sys import stdin

input = stdin.readline
ints = lambda : list(map(int, input().split()))

# 여기서 낭비가 큰듯
def arr_slice(x, y, size):
    sliced_elems = []
    for col in range(y, y+size):
        for row in range(x, x+size):
            sliced_elems.append(paper[col][row])
    
    return sliced_elems

# True라면 blue인지 white인지를 리턴, 아니면 False를 리턴
def check(x, y, size: int):
    checked = set(arr_slice(x, y, size))
    
    if len(checked) != 1:
        return False
    else:
        return checked.pop()+1

# 분할 함수
def divide(x, y, size):
    return [(x, y), (x+size//2, y), (x, y+size//2), (x+size//2, y+size//2),]

# DFS
def dfs(x, y, size):
    global blue, white
    criterion = check(x, y, size)

    if criterion:
        if criterion == 2:
            blue+=1
        else:
            white+=1
        return 
    else:
        divides = divide(x, y, size)
        for div in divides:
            x, y = div
            dfs(x, y, size//2)
    
# 메인 flow
if __name__ == "__main__":
    N = int(input())

    paper = [ints() for _ in range(N)]
    blue, white = 0, 0

    dfs(0, 0, N)

    print(white, blue, sep = "\n")
# 공백