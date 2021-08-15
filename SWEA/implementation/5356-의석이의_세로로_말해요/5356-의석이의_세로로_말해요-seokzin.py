from collections import deque

T = int(input())

for tc in range(1, T+1):
    words = []
    res = []

    for _ in range(5):
        words.append(deque(input()))  # words 내부엔 덱을 넣어 popleft() 사용

    while True:
        for word in words:
            if word:
                res.append(word.popleft())

        for word in words:  # 탈출 검증 파트
            if word:  # 덱이 안비었다면 탈출 X
                break  
        else:  # 덱이 비었다면 else에 도달. while 탈출
            break

    print(f"#{tc} ", *res, sep='')

# popleft()가 생각나 일부러 덱을 썼습니다. 리스트 안에 덱을 넣는 재밌는 경험이었습니다.
