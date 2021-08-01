import sys
input = sys.stdin.readline

members = {}

for _ in range(int(input())):
    age, name = input().split()
    age = int(age)
    if age in members:
        members[age].append(name)
    else:
        members[age] = [name]

for k, v in sorted(members.items(), key = lambda x: x[0]):
    for member in v:
        print(k, member)

"""
git commit -m "code: Solve boj 00000 문제 이름 (yeonhee)"
"""