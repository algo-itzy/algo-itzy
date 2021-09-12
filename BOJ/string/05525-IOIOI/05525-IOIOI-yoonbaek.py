# 완전 빠릅니다... 뿌듯
# 228ms

if __name__ == "__main__":
    N = int(input())
    M = int(input())

    P = "O".join("I"*(N+1))
    S = input()
    
    i, cnt = 0, 0
    # M-(2*N+1) : P와 비교할 수 있는 한계 범위
    while i < M-(2*N+1):
        # P의 길이만큼 비교 구문 실행
        for j in range(2*N+1):
            # 만약 같지 않으면, 같지 않은 지점으로 인덱스를 수정해주고 탈출
            if S[i+j] != P[j]:
                # O로 끝난 경우에는 그 다음부터 재탐색하도록 인덱스 변경
                if S[i+j] == "O":
                    i += j+1
                else:
                    i += j
                break
        # break에 걸리지 않고 일치할 경우
        else:
            # 찾았으므로 count 해주고 인덱스 바꿔줍니다.
            cnt += 1
            i += j+1
            # 다음 두개가 OI면 역시 또 다른 P를 찾은것 이기 때문에 간단히 비교해줍니다.
            while S[i:i+2] == "OI":
                cnt += 1
                i += 2
            # 아니라면 P 찾은 지점 다음부터 다시 최상위 while문으로 돌아가서 비교합니다.

    print(cnt)
# git commit -m "code: Solve boj 05525 IOIOI (yoonbaek)"