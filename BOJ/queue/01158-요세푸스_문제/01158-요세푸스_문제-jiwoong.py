# 요세푸스 순열
# 1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 순서대로 K번째 사람을 제거

n, k = map(int, input().split())
jose = [i for i in range(1, n + 1)]  # 초기 원탁에 앉아있는 사람들
ans = []  # 제거 value
num = 0  # 제거 인덱스 번호

for t in range(n):
    num += k - 1
    if num >= len(jose):  # 다시 롤백하는 경우 대비
        num = num % len(jose)
    ans.append(str(jose.pop(num)))
print("<", ", ".join(ans)[:], ">", sep='')
