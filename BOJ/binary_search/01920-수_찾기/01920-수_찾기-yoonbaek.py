# solved by YoonBaek
"""
해시 메모리로 풀었습니다만
이진 탐색을 배우는 문제이므로 이진 탐색으로 푸는게 맞는거 같습니다.
"""

def get_memory(n:int, ns:list) -> dict:
    memory = {}

    for n in ns:
        # 사실 아무거나 넣어도 됩니다.
        memory[n] = 1

    return memory

def solve(m: str) -> str :
    if memo.get(m):
        return "1\n"
    else:
        return "0\n"

if __name__ == "__main__":
    n = int(input())
    ns = input().split()

    memo = get_memory(n, ns)
    
    m = int(input())
    ms = input().split()
    
    result = ""
    for m in ms:
        result += solve(m)

    print(result[:-1])