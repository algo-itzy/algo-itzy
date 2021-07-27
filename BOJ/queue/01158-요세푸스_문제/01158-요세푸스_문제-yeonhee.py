import sys

input = sys.stdin.readline
N, K = map(int, input().split())

numbers = list(range(1, N+1))  # 일단 숫자를 뽑아서 쓸 리스트 만들기
josephus = []  # 요세푸스 순열 리스트 및 인덱스 초기화
idx = 0

while numbers:  # numbers에 값이 존재하지 않을때 까지
    # 인덱스를 이용해 numbers에서 pop(idx) 하게되면 다음 인덱스는 K-1을 더한 값이 됩니다.
    idx += K-1 
    idx %= len(numbers)  # numbers의 길이를 초과한 경우 len(numbers)로 나눈 나머지
    josephus.append(numbers.pop(idx))
    
print(f"<{', '.join(map(str, josephus))}>")