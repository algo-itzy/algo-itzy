T = int(input())                      # 테스트 케이스 개수

for _ in range(T):
    words = input().split()           # 리스트로 단어 간 분리
    for word in words:
        print(word[::-1], end = ' ')  # 단어별로 슬라이싱을 이용해 뒤집어서 출력