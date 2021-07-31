N = int(input())

word = []

for _ in range(N):
    word.append(input())

set_word =  list(set(word)) # set() 함수로 중복 제거

sort_word = []

for i in set_word:
     sort_word.append((len(i),i)) # 단어의 길이, 단어를 리스트에 저장하기

result = sorted(sort_word) #사전 순으로 정렬

for len_word, word in result:
    print(word)
