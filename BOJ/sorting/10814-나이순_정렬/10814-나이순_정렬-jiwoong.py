# 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬
# 각 회원의 나이와 이름이 공백으로 구분

import sys

n = int(sys.stdin.readline())
mems = []

for _ in range(n):
    mems.append(list(sys.stdin.readline().split()))
mems.sort(key=lambda x: int(x[0]))
for i in range(n):
    print(mems[i][0], mems[i][1])