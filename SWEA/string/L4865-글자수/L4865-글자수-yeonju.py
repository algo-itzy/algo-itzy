T = int(input()) 

for tc in range(T):
    N = input() # 길이가 N 인 문자열 str1
    M = input() # 길이가 M 인 뮨자열 str2

    letter = list(set(list(N))) 
    maximum = 0 

    for i in range(len(letter)):
        if M.count(letter[i]) > maximum :
            maximum = M.count(letter[i])

    print(f'#{tc+1} {maximum}')


# 첨엔 aba 이런 것도 하나의 글자라고 잘못 이해해서 이상하게 접근했었네요 (ㅋ_ㅋ)

# 중복되는 원소를 없애기 위해서 set() 함수를 사용 
# but set() 함수는 순서가 랜덤으로 나옴 
# 그렇기에 list로 set() 함수를 감싸주기