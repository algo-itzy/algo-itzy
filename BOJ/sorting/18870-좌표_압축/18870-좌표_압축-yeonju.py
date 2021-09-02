import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

nums2 = sorted(list(set(nums))) # set() 함수로 중복 제거 후, 오름차순 정렬

dic = {nums2[i]: i for i in range(len(nums2))}
for i in nums:
    print(dic[i], end =' ')

# nums2.index(i)로 하면 시간 초과
# 딕셔너리 형태로

# git commit -m "code: Solve boj 18870 좌표 압축 (yeonju)"