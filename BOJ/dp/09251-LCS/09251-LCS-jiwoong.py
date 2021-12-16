# git commit -m "code: Solve boj 09251 LCS (jiwoong)"
def lcs():
    str1, str2 = input(), input()
    arr = [[0 for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]

    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:  # 1번 문자열 = 2번 문자열 같으면
                arr[i][j] = arr[i - 1][j - 1] + 1  # 이전 lcs 길이 + 1
            else:  # 다르면
                arr[i][j] = max(arr[i - 1][j], arr[i][j - 1])  # 따로 한 글자씩 추가되었을 때 기준 큰 값
    print(arr[-1][-1])


if __name__ == '__main__':
    lcs()
