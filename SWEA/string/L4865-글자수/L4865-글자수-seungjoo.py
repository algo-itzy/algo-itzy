import sys
input = sys.stdin.readline
from collections import defaultdict

def count_chrs(s1, s2):
    char_set = defaultdict(int)
    for chr in s2:
        char_set[chr] += 1
    max_cnt = 0
    for char in s1:
        max_cnt = max(max_cnt,char_set[char])
    return max_cnt

    
for test in range(1,int(input())+1):
    str1 = input().rstrip()
    str2 = input().rstrip()
    print(f'#{test} {count_chrs(str1, str2)}')
