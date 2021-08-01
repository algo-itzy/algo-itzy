# solved by YoonBaek
"""
출력 방식이 속도를 결정하는 문제였습니다.

1. input 만큼 뱉어내므로 input만큼 효율적인 out을 쓰면 더 빠릅니다.
2. 나머지는 리스트에 메모리로 저장해서 풀었습니다.
   리스트 인덱스에 따라 자동 정렬 됩니다.
   메모리 보다는 시간 복잡도에 가중치
"""
from sys import stdin, stdout

# 감히 built-in 님들 이름 건드리기
input = stdin.readline
print = stdout.write

# 문제 조건 범위 설정
MAX = 1000000

def solve():
    n = int(input())

    # -100만 ~ 0 ~ 100만이기 때문에 크기르 200만 1개로 계산해 생성해줍니다.
    m = [False for _ in range(MAX*2+1)]

    # input으로 들어온 변수는 True를 켜줍니다.
    for _ in range(n):
        x = int(input())
        m[x+MAX] = True
    
    # -MAX가 0번째이므로 인덱스에서 -MAX해서 출력
    # elem이 True면 index print
    print("\n".join(map(str, [i-MAX for i, elem in enumerate(m) if elem])))

if __name__ == "__main__":
    solve()
