T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    
    dic = {}

    for c in set(str1):
        dic[c] = str2.count(c)

    print(f'#{tc}', max(dic.values()))

# 딕셔너리를 활용하래서 해봅니다.