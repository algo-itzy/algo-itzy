# solved by YoonBaek
# room을 400으로 잡으니 tc 9 / 10 pass라 고민 했습니다.
# 짝홀 ㅠ
# 동선 중간은 문제가 안되고 시작점과 끝점이 문제라
# 그 부분만 고려해서 풀었습니다

if __name__ == "__main__":
    T = int(input())

    for tc in range(1, T+1):
        N = int(input())
        
        rooms = [0] * (400 + 1)

        max_pass = 0
        for _ in range(N):
            start, end = map(int, input().split())
            
            if start > end:
                start, end = end, start

            if start%2 == 0:
                start -= 1
            if end%2 == 1:
                end += 1

            for i in range(start, end+1):
                rooms[i] += 1
                max_pass = max_pass if max_pass > rooms[i] else rooms[i]
            
        print(f"#{tc} {max_pass}")
        