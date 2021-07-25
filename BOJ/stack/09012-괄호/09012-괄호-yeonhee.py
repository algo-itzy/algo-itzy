T = int(input())                       # 테스트 데이터

def is_vps(ps):                        # return 쓰기위해 함수로 정의
    cnt = 0                            # 숫자로 체크
    for x in ps:
        if x == '(':
            cnt += 1
        elif x == ')':
            cnt -= 1
            if cnt == -1:              # 만약 중간에 cnt가 -1이되면 vps가 아님
                return 'NO'
    return 'YES' if cnt == 0 else 'NO' # 최종 숫자가 0이어야 vps

for _ in range(T):
    print(is_vps(input()))