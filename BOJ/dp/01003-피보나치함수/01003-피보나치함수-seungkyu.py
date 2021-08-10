def solve():
    t = int(input())

    for _ in range(t):

        num = int(input())
        # cnt[n]] = [fibo_0 연산 개수, fibo_1 연산 개수]
        cnt = [[1,0],  # 0일 때의 fibo_0은 1개, fibo_1은 0개
               [0,1]]  # 1일 때의 fibo_0은 1개, fibo_1은 0개
        # dp
        for i in range(2, num+1):
            # zip함수로 두 개 리스트의 같은 인덱스 더하기
            cnt.append(list(map(sum, zip(cnt[i-1], cnt[i-2]))))
        print(*cnt[num])

if __name__ == "__main__":
    solve()
