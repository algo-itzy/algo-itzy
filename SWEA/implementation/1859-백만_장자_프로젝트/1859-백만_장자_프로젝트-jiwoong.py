"""
# 백만 장자 프로젝트
연속된 N일 동안의 물건의 매매가를 예측
하루에 최대 1만큼 구입
판매는 얼마든지

첫 번째 줄에 테스트 케이스의 수 T
각 테스트 케이스 별로 첫 줄에는 자연수 N
둘째 줄에는 각 날의 매매가를 나타내는 N개의 자연수들이 공백으로 구분되어 순서대로

각 테스트 케이스마다 ‘#x’, 최대 이익을 출력
"""

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    buy = list(map(int, input().split()))
    hoard = 0

    sell = buy[N-1]
    # 뒤에서부터 읽기
    for i in range(N-2, -1, -1):
        # 매매가보다 작으면 판매
        if sell > buy[i]:
            hoard += sell - buy[i]
        # 매매가 갱신
        else:
            sell = buy[i]
    print(f'#{tc} {hoard}')
