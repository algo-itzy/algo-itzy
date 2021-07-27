# 원으로 돌아가는 자료구조, 끝 + 1 = 시작점이 되도록 설계
# 시작, 끝점을 가리키는 index를 만들기
# 큐로 푸는법 추가로 생각
n, k = list(map(int, input().split()))

# 나중에 합치기 편하게 하기 위해 숫자 대신 str로 만들어줌
yosebs = [f'{i+1}' for i in range(n)]
# 제거한 숫자 append할 리스트
answer = []
# 처음 제거 인덱스는 k가 아니라 k-1임을 유의
remove_idx = -1+k
# 리스트가 빌 때까지 진행
while len(yosebs) != 0:
    # 인덱스 넘어가면 % 이용해서 안에 오도록 설정 =가 들어가야함에 유의
    if remove_idx >= len(yosebs):
        remove_idx = remove_idx % len(yosebs)
    answer.append(yosebs[remove_idx])
    del yosebs[remove_idx]
    # 제거한 인덱스에서 k 만큼 더 이동해야 함 + 원소 개수가 한 개 줄었으므로 -1을 해줘야 함
    remove_idx += k - 1
        
answer = ', '.join(answer)
print(f'<{answer}>')
