# solved by YoonBaek
# 어차피 숫자 이름인 포켓몬은 없다고 생각해서,
# 그냥 key, val을 반전시켜서 Pokedex에 저장했습니다.
from sys import stdin, stdout

rd = stdin.readline
wr = stdout.write

if __name__ == "__main__":
    N, M = map(int, rd().split())

    Pokedex = {}
    for i in range(1, N+1):
        name = rd().rstrip()
        Pokedex[name] = i
        Pokedex[str(i)] = name

    for _ in range(M):
        query = rd().rstrip()
        wr(f"{Pokedex[query]}\n")