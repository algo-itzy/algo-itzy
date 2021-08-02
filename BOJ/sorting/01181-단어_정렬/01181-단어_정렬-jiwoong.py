# 단어 길이 짧은 것부터 -> 같으면 사전 순으로

n = int(input())
words = []

for _ in range(n):
    words.append(input())

words = list(set(words))  # 중복 단어 X
words.sort(key=lambda a: (len(a), a))  # 길이 같다면 사전 순으로 정렬, 짧은게 우선

print("\n".join(words))
