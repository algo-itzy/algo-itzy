"""
리스트 내 딕셔너리 정렬 이용
age로 먼저 정렬 후, 들어온 순서(숫자)로 추가 정렬
"""
import sys


def solve():
    input = sys.stdin.readline
    n = int(input())
    names = []
    # 리스트 내에 한사람 정보씩 딕셔너리 1개 만들어서 append
    for idx in range(n):
        person = {}
        age, name = input().split()
        person["age"] = int(age)
        person["name"] = name
        person["order"] = idx
        names.append(person)

    # 정렬 2번
    sorted_person = sorted(names, key=lambda x: (x["age"], x["order"]))
    for person in sorted_person:
        print(person["age"], person["name"])


if __name__ == "__main__":
    solve()
