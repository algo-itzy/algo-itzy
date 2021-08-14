
# 그냥 손에 익힐겸 KMP 알고리즘.
# 개인적인 연습으로 따로 설명은 없어도 될것 같습니다.

# 손실함수 table 만드는 함수
def make_pattern(s):
    counter = 0
    for idx in range(1, len(s)):
        # pattern 내부에서 순회하며 counter 포인터와 idx포인터가 
        # 가르키는 문자가 같지 않으면 실패지점으로 돌아갑니다
        while counter > 0 and s[counter] != s[idx]:
            counter = lose_funtion[counter-1]
        # 같다면 매칭된 길이만큼 적어두고 차후 실패했을 시 돌아갈 idx로 활용합니다.
        if s[counter] == s[idx]:
            counter += 1
            lose_funtion[idx] = counter


# 패턴 매칭 시키는 함수.
def KMP_pattern_matching(p, s):
    counter = 0
    p_size = len(p)
    # 패턴을 매칭시킬 문자열 s를 순회합니다
    for idx in range(len(s)):
        # pattern 내부를 도는 counter 포인터와 s문자열을 도는 idx로 일치여부를 판별합니다.
        while counter > 0 and p[counter] != s[idx]:
            counter = lose_funtion[counter-1]
        #  같다면 counter를 늘려 다음 문자가 일치하는지 여부를 확인합니다.
        if p[counter] == s[idx]:
            # 일치하는 숫자의 길이가 패턴 문자열만큼이 되면 성공을 리턴합니다.
            if counter == p_size - 1:
                return 1
            else:
                counter += 1
    return 0

for test in range(1,int(input())+1):
    str1 = input().rstrip()
    str2 = input().rstrip()

    lose_funtion = [0 for _ in range(len(str1))]
    make_pattern(str1)
    print(f'#{test} {KMP_pattern_matching(str1, str2)}')
