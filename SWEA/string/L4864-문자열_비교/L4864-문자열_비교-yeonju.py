T = int(input())        #  테스트 케이스의 개수 T

for tc in range(T):
    N = input()         # str1 ab
    M = input()         # str2 abcdefg
    ans = 0 
    for i in range(len(M) - len(N) +1):
        for j in range(len(N)):
            if M[i+j] != N[j]:
                break   # 앞에서부터 한글자라도 틀리면 문자 비교 멈추기
        else:           # for .. else : for 문 다 돌고나서 else 로 
            ans = 1     # 있는지 없는지만 확인하면 되기에, 하나 찾고나서 바로 break 
            break

    print(f'#{tc+1} {ans}')


