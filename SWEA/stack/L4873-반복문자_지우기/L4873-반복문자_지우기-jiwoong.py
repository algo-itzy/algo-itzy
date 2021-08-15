"""
# 반복문자 지우기
지워진 부분은 다시 앞뒤를 연결, 또 반복문자가 생기면 이부분을 다시 지우기
반복문자를 지운 후 남은 문자열의 길이를 출력, 남은 문자열이 없으면 0을 출력

테스트 케이스 개수 T
문자열

#과 1번부터인 테스트케이스 번호, 빈칸에 이어 답을 출력
"""

T = int(input())
for tc in range(1, T + 1):
    words = input()
    repeat = []

    for word in words:
        if not repeat:
            repeat.append(word)  # 빈 스택
        elif word != repeat[-1]:  # 다를 때
            repeat.append(word)
        else:
            repeat.pop()
    print(f'#{tc} {len(repeat)}')
