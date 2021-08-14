# solved by YoonBaek
def is_palindrome(length: int, word: str) -> bool:
    min_idx, max_idx = 0, length-1

    while min_idx <= max_idx:
        if word[min_idx] != word[max_idx]:
            return False
        else:
            min_idx += 1
            max_idx -= 1
        
    return True


if __name__ == "__main__":
    T = int(input())
    
    for tc in range(1, T+1):
        N, M = map(int, input().split())
        palindrome = ""
        palindromes = []

        # 가로방향은 그냥 입력 받을 때 검사해버립니다.
        for _ in range(N):
            row = input()

            for i in range(N-M+1):
                check = row[i:i+M]
                # 여기서 break를 하면 input에서 오류가 나기 때문에 계속 진행합니다.
                if is_palindrome(M, check):
                    palindrome = check
            
            palindromes.append(row)
        
        # 가로 방향에서 안나오면 마지못해 세로 방향을 해봅니다.
        if not palindrome:    
            for col in range(N):
                target = ""
                for row in range(N):
                    target += palindromes[row][col]
                
                for i in range(N-M+1):
                    check = target[i:i+M]
                    if is_palindrome(M, check):
                        palindrome = check
                        break
        
        # 최종 결과를 출력합니다.
        print(f"#{tc} {palindrome}")