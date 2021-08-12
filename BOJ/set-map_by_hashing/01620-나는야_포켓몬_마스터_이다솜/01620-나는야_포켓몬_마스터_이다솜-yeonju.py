import sys

input = sys.stdin.readline
N, M = map(int, input().split()) # N 은 포켓몬의 개수, M 은 맞춰야하는 문제 개수 

dict ={}                         # 포켓몬 번호와 이름의 짝을 담을 dictionary 선언

for i in range(1, N+1):          # 포켓몬 번호와 이름 입력 받기
    name = input().strip()
    dict[i] = name
    dict[name] = i

# print(dict)

for j in range(M):
    poket = input().strip()
    if poket.isdigit():         # 포컷몬 번호로 주어지면, 이름을 출력
        print(dict[int(poket)]) # 참고로, input 값이 string 이었기에, 숫자로 받기 위해 int 로 감싸줘야 함!

    else:                       # 포켓몬 이름으로 주어지면
        print(dict[poket])


"""
포켓몬의 번호 뿐만 아니라, 이름도 key 의 값에 넣어 줘야하는 게 핵심이었던 듯?!
"""