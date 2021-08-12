 # solved by YoonBaek 

# 아이디어
# 1. 회의실을 빨리 비워줘야 다음 사람이 쓸 시간이 많이 남는다
#    종료 시간을 기준으로 정렬하고, 겹치는 회의를 빼고 카운트 하자
#    제출 : 80% 지점에서 오답

# 2. 예외를 찾아봄
#    그 결과 end로만 정렬할 경우
#    6 6
#    4 6 같은 순서를 처리하기 어려움을 발견
#    4 6 - 6 6은 둘 다 가능하나 6 6 - 4 6은 한 회의 밖에 안 됨
#    이중 정렬 인덱스 추가 후 solve
import sys

rd = sys.stdin.readline

if __name__ == "__main__":
    N = int(rd().rstrip())

    meetings = []
    for _ in range(N):
        meeting = list(map(int, rd().split()))
        meetings.append(meeting)

    meetings = sorted(meetings, key=lambda x : (x[1], x[0]))
    
    prev_end = cnt = 0
    for meeting in meetings:
        start, end = meeting
        if start >= prev_end:
            cnt += 1
            prev_end = end

    print(cnt)