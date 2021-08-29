import sys
input = sys.stdin.readline

m = int(input())                    # 연산의 수 m 

s = set()
s_all = set(map(str, range(1, 21))) # 미리 안 만들어 놓으면 시간 초과

for i in range(m):
    c = input().split()
    
    if c[0] == 'add':               # 어짜피 set() 함수는 중복값을 저장 안 하니, add 하는 수 모두 더해줘도 상관 x 
            s.add(c[1])
    elif c[0] == 'remove':
        if c[1] in s:
            s.remove(c[1])
    elif c[0] == 'check':
        if c[1] in s:
            print(1)
        else: 
            print(0)
    elif c[0] == 'toggle':
        if c[1] in s:
            s.remove(c[1])
        else:                       # s 에 해당되는 값이 안 들어있으면
            s.add(c[1]) 
    elif c[0] == 'all':
            s = s_all
    elif c[0] == 'empty':
        s.clear()


# pop()- 삭제하려는 값의 인덱스 입력 vs remove() - 삭제하려는 값 직접 입력

# git commit -m "Solve boj 11723 집합 (yeonju)"