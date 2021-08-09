import sys
input = sys.stdin.readline

n, m = map(int, input().split())

never_heard = set([input().strip() for _ in range(n)])
never_seen = set([input().strip() for _ in range(m)])

never_heard_and_seen = never_heard & never_seen
never_heard_and_seen = sorted(list(never_heard_and_seen))

print(len(never_heard_and_seen))
print(*never_heard_and_seen, sep='\n')
