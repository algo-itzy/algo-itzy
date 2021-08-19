# solved by YoonBaek

if __name__ == "__main__":
    T = int(input())

    for tc in range(1, T+1):
        N = int(input())

        # 정류장 리스트 생성
        routes = [0] * (5000+1)
        # 정류장별 버스 수++
        for _ in range(N):
            start, end = map(int, input().split())
            for i in range(start, end+1):
                routes[i] += 1
        
        P = int(input())
        ans = []
        
        print(f"#{tc}", end=" ")
        for _ in range(P):
            j = int(input())
            ans.append(routes[j])
        # 출력할 게 많으므로 한 번에 출력
        print(*ans)