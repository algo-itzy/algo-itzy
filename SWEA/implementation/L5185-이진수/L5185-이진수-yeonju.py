# 16진수를 4자리 2진수로

dic = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

t = int(input())

for tc in range(t):
    ans = ''
    n, sixteen = input().split()
    sixteen[::-1]                               # 뒤에서부터 정렬하기 -> 기존 값의 제일 왼쪽에 위치하던 값으로 인덱스 접근 용이
    for i in range(int(n)):
        if sixteen[i].isdigit():                # 숫자이면
            temp = bin(int(sixteen[i]))[2:]
            temp_len = 4 - len(temp)            # 2진수를 4자리로 채우기 위해
            ans = ans + '0' * temp_len + temp
        else:                                   # 숫자 아니고 알파벳이면
            temp = dic[sixteen[i]]
            ans = ans + bin(int(temp))[2:]
    print(f'#{tc+1}', ans)


# 10진수 32를 2진수로 변환하기
# a = 32
# binary_a = bin(a)
# print(binary_a)
# 결과값: 0x20



# git commit -m "code: Solve swea L5185 이진수 (yeonju)"