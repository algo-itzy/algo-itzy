import sys
input = sys.stdin.readline

numbers = [int(input()) for _ in range(int(input()))]
print('\n'.join(map(str, sorted(numbers))))


"""
git commit -m "code: Solve boj 02751 수 정렬하기 2 (yeonhee)"
"""