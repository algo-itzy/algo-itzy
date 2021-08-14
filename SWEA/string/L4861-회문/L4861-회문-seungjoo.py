import sys
input = sys.stdin.readline

# 회문을 찾자
def find_palindrome(N,M,sentences):
    # 행 순회
    for i in range(N):
        for j in range(N-M+1): # 열(시작점 인덱스) 순회(패턴 길이만큼 제외)
            if sentences[i][j] == sentences[i][j+M-1]: #문자열의 양끝 같으면
                left = j
                right = j+M-1
                while sentences[i][left] == sentences[i][right] and left <= right: # 안으로 파고들며 매칭
                    left += 1
                    right -= 1
                if left < right: # 반복문이 중간에 깨졌으면 회문 아니니 속행
                    continue
                else:
                    return sentences[i][j:j+M] # 반복문이 무사히 완료됐으면 회문이니 반환 출력.

for test in range(1,int(input())+1):
    N, M = map(int,input().split())
    palindrome = list(list(input().rstrip()) for _ in range(N))
    result1 = find_palindrome(N,M,palindrome)
    if result1:
        print(f"#{test} {''.join(result1)}")
    else:
        reverse_palindrome = list(zip(*palindrome)) # 문자열 열, 횡 뒤집기.
        result2 = find_palindrome(N,M,reverse_palindrome)
        print(f"#{test} {''.join(result2)}")