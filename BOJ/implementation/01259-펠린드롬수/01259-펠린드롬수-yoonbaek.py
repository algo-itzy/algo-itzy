# solved by YoonBaek
"""
python으로는 너무나도 쉽게 풀 수 있는 문제
그냥 iterable한 str 형태를 유지하며 풀었다.
"""
from sys import stdin

# solve1
# 이건 아무리 긴 숫자라도 다 뒤집고 보기 때문에 조금 느립니다.
def is_palindrome(num: str) -> None:
    print("yes" if num == num[::-1] else "no")

# solve2
# 이건 회문이 아니라고 판단되는 순간 프로그램을 끝내버리기 때문에
# 조금이나마 더 빠릅니다
def is_palindrome_search(num: str) -> None:
    num_len = len(num)

    for i in range(num_len):
        if num[i] != num[num_len-1-i]:
            print("no")
            return
            
    print("yes")

if __name__ == "__main__":
    nums = stdin.read().rstrip().split()
    nums = nums[:-1]

    for num in nums:
        is_palindrome_search(num)

"""
git commit -m "code: Solve boj 01259 펠린드롬수 (yoonbaek)"
"""
