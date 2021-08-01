N = input() # 수의 개수

numbers = list(map(int, input().split())) # 소수인지 판별해야될 수를 리스트에 담음
cnt = 0 # 소수의 개수

for num in numbers:
    if num == 1: # 1이면 스킵
        continue

    elif num == 2: 
        cnt += 1

    else: # 2 이상인 수들을 나눴을 때 나머지가 0이 안나오면 소수이기에 cnt 추가
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            cnt += 1

print(cnt)




# 소수 : 1보다 큰 자연수 중 1과 자기 자신만을 약수로 가지는 수
