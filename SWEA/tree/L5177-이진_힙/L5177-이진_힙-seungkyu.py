import sys
sys.stdin = open('input2.txt')
# 주어진 조건과 다르게 tree 인덱스가 0부터 시작하는 것으로 짯습니다.

def make_b_tree():  # 이진 힙 만들기
    for i, num in enumerate(numbers):  
        b_tree.append(num)  # 순차적으로 값 하나하나 넣어줌
        idx = i  # 끝 지점 인덱스값 idx에 업데이트
        while idx:  # idx가 0일 때까지 진행
            if b_tree[(idx-1)//2] > b_tree[idx]:  # 부모값이 크면 서로 자리 바꾸기
                b_tree[idx], b_tree[(idx-1)//2] = b_tree[(idx-1)//2], b_tree[idx]
                idx = (idx-1)//2
            else:
                break
        

def calculate():
    idx = N-1 # 인덱스 주의
    ans = 0
    while idx:
        ans += b_tree[(idx-1)//2]  # 위로 올라가면서 값 더해주기
        idx = (idx-1)//2  # 인덱스 부모값으로 변경
    return ans

T = int(input())
for test_case in range(1, T+1):

    N = int(input())
    b_tree = []
    numbers = list(map(int, input().split()))
    make_b_tree()
    ans = calculate()
    print(f'#{test_case} {ans}')
