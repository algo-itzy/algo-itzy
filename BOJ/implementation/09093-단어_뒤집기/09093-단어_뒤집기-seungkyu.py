# 테스트 개수 입력
test_case = int(input())

for _ in range(test_case):
    # 공백을 기준으로 단어들을 나눠 리스트에 저장
    sentences = list(map(str, input().split()))
    # 단어들을 각각 거꾸로 출력, 뒤에 띄어쓰기 추가
    for word in sentences:
        print(word[::-1], end=' ')
    # 개행
    print()