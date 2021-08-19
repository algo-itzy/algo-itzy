# solved by YoonBaek
# output을 꼭 그렇게 받아야만 했니

def rotate90(arr: list):
    return [i[::-1] for i in zip(*arr)]

if __name__ == "__main__":
    T = int(input())

    for tc in range(1, T+1):
        N = int(input())

        r0 = []
        for _ in range(N):
            r0.append(list(map(int, input().split())))

        # 90도씩 회전
        r90 = rotate90(r0)
        r180 = rotate90(r90)
        r270 = rotate90(r180)

        print(f"#{tc}")
        for row in range(N):
            print(*r90[row], sep = "", end= " ")
            print(*r180[row], sep = "", end= " ")
            print(*r270[row], sep = "")