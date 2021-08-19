t = int(input())

for tc in range(t):
    arr = [input() for _ in range(5)] # 다섯개의 단어들 입력 받기 

    m = 0                             # 다섯개 단어 중 가장 긴 단어의 길이 m
    for i in range(5):
        if len(arr[i]) > m:
            m = len(arr[i])
 

    for i in range(5):              
        difference = m - len(arr[i])  # 가장 긴 단어와 차이가 나는 것 만큼 공백을 '-'로 채우기

        arr[i] += '-' * difference    # 그러면 모든 단어의 길이 통일 가능


    ans =''                           # 정답을 담을 ans 생성
    for i in range(m):                # arr 에 담아놨던 단어 배열을 세로로 읽기
        string =''

        for j in range(5):
            if arr[j][i] != '-':      # '-' 가 들어간 부분은 스킵하며 더해ㅐ가기
                string += arr[j][i]
        ans += string

    print(f'#{tc+1} {ans}')


# 아래는 실패한 거여서 안 읽으셔도 됩니다! :) 
# # 1차 시도
# t = int(input())
#
# for tc in range(t):
#     arr = [list(input()) for _ in range(5)]
#     vertical = []
#
#     m = 0
#     for i in range(5):
#         if len(arr[i]) > m:
#             m = len(arr[i])
#     print(m)
#
#     for i in range(5):
#         for j in range(m):
#             if arr[i][j]:
#                 vertical.append(arr[i][j])
#
#     print(vertical)


# 2차 시도
# 봉착점: 길이가 짧은 문자열은 안 나옴
# t = int(input())

# for tc in range(t):
#     arr = [input() for _ in range(5)] # ['adf','dfsd','asdf']
#     b=list(zip(*arr))
#     print(b)






