# 검은색- 0 - 못 들어감 
# 흰색 - 1

# 으아악!! 몇 개 밖에 통과를 못해서,,, 좀 더 찾아보겠습니다 ㅠ-ㅠ
t = int(input())

for tc in range(t):
    n, k = map(int, input().split())                            # 가로, 세로 길이 n / 단어의 길이 k

    arr = [list(map(int, input().split())) for _ in range(n)]   # 퍼즐을 arr 에 담기
    cnt = 0                                                     # 길이가 k 인 단어들 카운트할 변수 cnt


    for i in range(n):                                          # 행 탐색
        for j in range(0, n- k +1):                             # 열 탐색
            block1 = 0
            block2 = 0
            for l in range(k):                                  # k 의 길이인 블럭이 있나 확인
                if arr[i][j+l] == 1:                            # 가로 블럭 확인
                    block1 +=1
            if block1 == k:
                cnt +=1

            for l in range(k):
                if arr[j+l][i] == 1:                            # 세로 블럭 확인
                    block2 += 1
            if block2 == k:
                cnt +=1


    print(f'#{tc+1} {cnt}')

