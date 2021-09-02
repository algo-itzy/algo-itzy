N = int(input())            # 이동하려고 하는 채널
M = int(input())            # 고장난 버튼의 개수
broken = input().split()    # 고장난 버튼

result = abs(100 - N)       # 현재 채널인 100에서 + 이나 - 로 이동할 경우 (초기화)

for num in range(1000001):  # 작은 수 -> 큰 수로 이동하는 경우와 큰수 -> 작은 수로 이동하는 경우 모두 포함
    for i in str(num):      # 현재 순회중인 채널의 각 자리수
        if i in broken:     # 이 버튼이 망가졌으면 다시 순회하러 간다.
            break
    else:                   # 번호를 눌러서 만들 수 있으면 최솟값 갱신
        result = min(result, len(str(num)) + abs(num - N))  # 번호를 누른 횟수 + 해당 번호로부터 타겟까지의 차이

print(result)


"""
무지성으로 풀다가 안풀려서 다른 풀이 참고했습니다 ㅠㅠ
아이디어가 어렵네요.
"""
