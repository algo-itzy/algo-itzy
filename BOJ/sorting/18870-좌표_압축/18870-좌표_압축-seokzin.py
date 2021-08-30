n = int(input())

rank = {}  # 요소-순위 쌍을 담음
arr = list((map(int, input().split())))
arr_sort = sorted(list(set(arr)))

for i in range(len(arr_sort)):
    rank[arr_sort[i]] = i

for x in arr:
    print(rank[x], end=' ')

# 요소들의 순위를 출력해야 함. 근데 정렬하면 인덱스가 곧 순위가 됨.