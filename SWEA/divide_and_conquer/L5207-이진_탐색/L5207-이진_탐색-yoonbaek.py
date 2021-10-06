ints = lambda: map(int, input().split())

def binary_search(start, end, target, flag):
    while start <= end:
        mid = (start+end)//2
        if target > A[mid]:
            start = mid+1
            if flag[-1] != "R":
                flag += "R"
            else:
                return
        elif target < A[mid]:
            end = mid-1
            if flag[-1] != "L":
                flag += "L"
            else:
                return
        else:
            return flag
    
    return


if __name__ == "__main__":
    T = int(input())

    for tc in range(1, T+1):
        N, M = ints()
        A = sorted(list(ints()))
        B = list(ints())
        cnt = 0

        for num in B:
            flag = binary_search(0, N, num, " ")
            if flag:
                cnt += 1

        print(f"#{tc} {cnt}")
# git commit -m "code: Solve swea L5207 이진 탐색 (yoonbaek)"