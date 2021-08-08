import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dic_idx = {}  # idx: name 쌍
dic_name = {}  # name: idx 쌍

for idx in range(1, n+1):
    name = input().rstrip()  # \n 제거
    dic_idx[idx] = name 
    dic_name[name] = idx

for _ in range(m):
    q = input().rstrip() 

    print(dic_name[q]) if q.isalpha() else print(dic_idx[int(q)])

# Value로 Key 출력 방법 - dict를 뒤집어 Value-Key dic을 만든다.
# 사실 더 좋은 풀이가 있을 것 같지만 이 정도에서 마무리 합니다.
