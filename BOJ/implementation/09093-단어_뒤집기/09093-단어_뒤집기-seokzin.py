t = int(input())

for i in range(t):
  words = list(input().split())

  for word in words:
    # 단어를 뒤집으면서 바로 출력 / sep, end를 통해 출력 다듬기
    print(*reversed(word), sep='', end=' ') 