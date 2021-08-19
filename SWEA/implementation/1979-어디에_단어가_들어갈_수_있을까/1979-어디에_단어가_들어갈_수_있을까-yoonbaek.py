# solved by YoonBaek

if __name__ == "__main__":
 
    T = int(input())
 
    for tc in range(1, T+1):
        N, K = map(int, input().split())
 
        puzzle = [list(map(int, input().split())) for _ in range(N)]
 
        cnt = 0
        for col in range(N):
            v_cnt, h_cnt = 0, 0
            for row in range(N):
                v = puzzle[row][col]
                h = puzzle[col][row]
                
                # 1을 만났을 때는 카운트++
                if v: 
                    v_cnt += 1
                # 0을 만났을 때 체크하고 숫자 세기
                else:
                    if v_cnt == K:
                        cnt += 1
                    v_cnt = 0
                # 1을 만났을 때는 카운트++
                if h: 
                    h_cnt += 1
                # 0을 만났을 때 체크하고 숫자 세기
                else:
                    if h_cnt == K:
                        cnt += 1
                    h_cnt = 0

             # 마지막에 0을 만나지 못하고 종료될 경우 예외처리
            if v_cnt == K:
                cnt += 1
            if h_cnt == K:
                cnt += 1
 
        print(f"#{tc} {cnt}")
