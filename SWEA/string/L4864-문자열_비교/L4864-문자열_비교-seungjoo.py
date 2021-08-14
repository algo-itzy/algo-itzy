
# 그냥 손에 익힐겸 KMP 알고리즘.
#  개인적인 연습으로 따로 설명은 없어도 될것 같습니다.

# 손실함수 table 만드는 함수
def make_pattern(s):
    counter = 0
    for idx in range(1, len(s)):
        while counter > 0 and s[counter] != s[idx]:
            counter = lose_funtion[counter-1]
        if s[counter] == s[idx]:
            counter += 1
            lose_funtion[idx] = counter


# 패턴 매칭 시키는 함수.
def KMP_pattern_matching(p, s):
    counter = 0
    p_size = len(p)
    for idx in range(len(s)):
        while counter > 0 and p[counter] != s[idx]:
            counter = lose_funtion[counter-1]
        if p[counter] == s[idx]:
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
