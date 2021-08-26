t = int(input())

for tc in range(t):
    n, m, k = map(int, input().split())         # 주어지는 숫자(1000 이하), 지정위치부터 m 칸 추가, k 회 반복 
    nums = list(map(int, input().split())) 

    index = 0                                   # 시작점 인덱스 0으로 초기화 

    for i in range(k):
        index += m

        index %= len(nums)

        if index ==0:                           # 배열의 마지막 원소로 도착하게 되면
            nums.append(nums[0]+ nums[-1])
            index -= 1
        
        else: 
            nums.insert(index, nums[index-1]+ nums[index])
        
    print(f'#{tc+1}', *nums[::-1][:10])         # 10개까지만 역순으로 출력 

 