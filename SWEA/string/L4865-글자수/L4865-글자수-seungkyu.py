import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T+1):

    N = input()
    M = input()

    word_dict = {}  # M 한바퀴 돌면서 딕셔너리 생성
    for char in M:
        if char not in word_dict:
            word_dict[char] = 1
        else:
            word_dict[char] += 1

    max_num = 0
    for char in N:  # N 글자를 한바퀴 돌면서 max 찾기
        if max_num < word_dict[char]:
            max_num = word_dict[char]

    print(f'#{test_case} {max_num}')