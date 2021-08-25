for tc in range(1, int(input())+1):
    N, M, L = map(int, input().split())
    nums = list(map(int, input().split()))

    for _ in range(M):
        nums.insert(*map(int, input().split()))
        
    print(f'#{tc}', nums[L])

# map도 구조 분해 할당이 되는 것이 신기했습니다.
# 더 나은 풀이가 있겠지만 대충 insert로 풀었습니다. 
