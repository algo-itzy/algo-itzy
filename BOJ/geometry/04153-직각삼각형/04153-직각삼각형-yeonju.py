"""
각 테스트케이시는 모두 30,000보다 작은 양의 정수
입력 마지막 줄에는 000
"""

tri = list(map(int, input().split()))

while tri!=[0,0,0]: # 0 0 0 이 나오면 종료

    tri.sort() # 오름차순 배열

    if tri[2]**2 == tri[0]**2 + tri[1]**2: # 직각 삼각형 구하는 공식 사용
        print('right')
        
    else: print('wrong')
    tri = list(map(int, input().split()))




"""
git commit -m "code: Solve boj 00000 문제 이름 (yeonju)"
"""