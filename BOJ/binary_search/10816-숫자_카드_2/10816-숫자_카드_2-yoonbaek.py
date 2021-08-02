# solved by YoonBaek
"""
아니 이진 탐색 문제라메!!!!!!!!!!!!!!!!!!
안 풀리자나

담엔 걍 해시 메모리로 풀어야지
이진 탐색 연습해본다고 어거지로 풀어봤습니다.

1. have[mid] == ask 일 때 count 사용
--> 17% 지점 시간 초과
2. count 제거. mid 주변 탐색
--> 33% 지점 시간 초과
3. 설마 테스트 케이스에 중복 있겠나 싶어서 
solved dict 생성 후 binary_search 호출 중복 제거
--> 통과

어휴....
"""

from sys import stdin, stdout
from typing import Tuple
read = stdin.read

def input() -> Tuple[int, list, list]:
    r = read().rstrip().split("\n")

    n = int(r[0])
    have = list(map(int, r[1].split()))
    asks = list(map(int, r[-1].split()))

    return n, have, asks

def binary_search(n: int, have: list, ask: int) -> int:
    cnt, start, end = 0, 0, n-1

    while start <= end:
        mid = (start+end)//2
        if have[mid] > ask:
            end = mid-1
        elif have[mid] < ask:
            start = mid+1
        else:
            cnt+=1
            now = mid-1
            while now >= start and have[now]==ask:
                now-=1
                cnt+=1

            now = mid+1
            while now <= end and have[now]==ask:
                now+=1
                cnt+=1 

            return cnt

    return cnt

if __name__ == "__main__":
 
    n, have, asks = input()
    have = sorted(have)
    ans, solved = [], {}
    for ask in asks:
        check = solved.get(ask)
        
        if check:
            a =  check
        else :
            a = binary_search(n, have, ask)
            solved[ask] = a  

        ans.append(a)

    print(" ".join(list(map(str, ans))))