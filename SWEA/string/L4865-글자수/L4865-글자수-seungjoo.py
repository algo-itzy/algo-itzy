import sys
input = sys.stdin.readline
from collections import defaultdict

def count_chrs(s1, s2):
    char_set = defaultdict(int) # deault값 입력을 자동화하기 위해 defaultdict사용했습니다
    for chr in s2:
        char_set[chr] += 1
    max_cnt = 0
    for char in s1: # s1문자열에 들어있는 문자의 수를 세줬습니다
        max_cnt = max(max_cnt,char_set[char])
    return max_cnt

    
for test in range(1,int(input())+1):
    str1 = input().rstrip()
    str2 = input().rstrip()
    print(f'#{test} {count_chrs(str1, str2)}')
