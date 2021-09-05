# solved by YoonBaek

def get_gcd(l: int, r: int) -> int:
    # 최대공약수 : 유클리드 호제법 참고해서 구현했습니다.
    # O(n)보다 빠른 O(logn)이라고 합니다.
    l, r = (r, l) if l < r else (l, r)
    mod = l % r

    # if mod == 0 break, else recurse
    return r if not mod else get_gcd(r, mod)

def get_lcm(gcd: int, l: int, r: int) -> int:
    return l*r // gcd

if __name__ == "__main__":
    l, r = map(int, input().split())
    gcd = get_gcd(l, r)
    lcm = get_lcm(gcd, l, r)

    print(gcd, lcm, sep = "\n")

"""
git commit -m "code: Solve boj 00000 문제 이름 (yoonbaek)"
"""