import sys
sys.stdin = open('sample_input 2.txt')

T = int(input())

for test_case in range(1, T+1):
    words = []
    for _ in range(5):
        words += input().split()

    words_t = [[] for _ in range(15)]  # 제일 긴 길이가 15라고 해서 배열을 만들었습니다.
    
    for word in words:
        for idx, chr in enumerate(word):  # ex) 4글자이면 words_t[4]에 저장되도록
            words_t[idx] += chr
    
    
    print(f'#{test_case}', end=' ')
    for words in words_t:
        print(*words, sep='' ,end='')
    print()
