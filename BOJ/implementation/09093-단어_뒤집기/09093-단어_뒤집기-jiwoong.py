# 단어 뒤집기

T = int(input())  # 테스트 케이스의 개수 T

for i in range(T):  # T 인풋으로 반복 횟수

    sen = input()  # 문장 input
    word = list(sen.split(' '))  # 인풋 문장 리스트화

    for j in word:  # 리스트 내 반복
        print(j[::-1], end=' ')  # 공백을 두고 하나씩 출력
    print()

# 한꺼번에 출력은 어떻게 해야할까요..
