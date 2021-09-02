# git commit -m "code: Solve boj 01107 리모컨 (yoonbaek)"
# 도르마무를 해야하는 문제
# 자꾸 EOF로 틀리네요.... 테케 모두 통과되면 수정하겠습니다.

if __name__ == "__main__":
    target_channel = input()
    length = len(target_channel)
    target_channel = int(target_channel)

    broken_num = int(input())
    broken_buttons = []
    if broken_num:
        broken_buttons = input().split()

    worst = abs(target_channel-100)
    minimum = worst

    scope = range(2*10**length) # 타깃과 1로 시작하는 그 다음자리 수까지 비교하기 위함
    for num in scope:
        digits = str(num)
        for digit in digits:
            if digit in broken_buttons:
                break
        else:
            steps = len(digits) + abs(target_channel-num)
            minimum = minimum if steps > minimum else steps
        
    print(minimum)