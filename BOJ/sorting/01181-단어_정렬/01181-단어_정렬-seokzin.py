n = int(input())

words = []

for _ in range(n):
  words.append(input())

words = list(set(words))  # 중복 제거
words.sort()  # 사전순 정렬
words.sort(key=lambda x: len(x))  # 길이순 정렬

print(*words, sep='\n')

# 정렬 순서가 중요하다!