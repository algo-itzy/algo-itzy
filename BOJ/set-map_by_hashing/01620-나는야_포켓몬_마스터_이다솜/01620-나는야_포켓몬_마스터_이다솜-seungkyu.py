import sys

input = sys.stdin.readline
N, M = map(int, input().split())

# key가 이름일 때와 번호일 때 2가지 경우 모두 사용되므로 2개 dict 사용
pokemon_key_num = {}
pokemon_key_name = {}

for i in range(1,N+1):
    poke_name = input().strip()
    # input 받아서 2개의 dict에 모두 넣어주기
    pokemon_key_num[i] = poke_name
    pokemon_key_name[poke_name] = i

for _ in range(M):
    test = input().strip()
    # 원래는 str이므로 int 변환 시 오류나는지에 따라 구분
    try:
        test = int(test)
        print(pokemon_key_num[test])
    except:
        print(pokemon_key_name[test])
