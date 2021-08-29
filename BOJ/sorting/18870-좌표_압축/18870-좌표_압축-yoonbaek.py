# solved by YoonBaek
if __name__ == "__main__":
    N = int(input())
    numbers = list(map(int, input().split()))
    # 중복을 제거하고 정렬합니다.
    duple_check = sorted(list(set(numbers)))

    # duple_check의 인덱스와 값으로 hash를 구성합니다.
    HASH = {}
    for idx, val in enumerate(duple_check):
        HASH[val] = idx

    # 해쉬를 참조해 결과 출력
    f = lambda x: str(HASH[x])

    print(" ".join(map(f, numbers)))

# git commit -m "code: Solve boj 18870 좌표 압축 (yoonbaek)"