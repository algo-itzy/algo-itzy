class Member:
    def __init__(self, group=None):
        self.group = group
        

if __name__ == "__main__":
    T = int(input())

    for tc in range(1, T+1):
        N, M = map(int, input().split())
        members = list(map(int, input().split()))
        is_joined = [0] * (N+1)

        cnt = N
        for i in range(0, 2*M, 2):
            a, b = members[i], members[i+1]
            # 둘 다 아직 그룹이 없을 때, 새 그룹이라고 생각하고 그룹 카운트에서 빼줌
            # 둘은 소속 그룹이 생긴 것이므로 is_joined 배열에 표기
            if not is_joined[a] and not is_joined[b]:
                cnt -= 1
                is_joined[a] = Member(cnt)
                is_joined[b] = Member(cnt)
            # 한 쪽이 그룹이 있을 때, 나머지 인원은 한쪽 그룹에 복속
            # 이 경우, 단독 그룹이 사라지므로 카운트가 줄어듬
            elif is_joined[a] and not is_joined[b]:
                cnt -= 1
                is_joined[b] = Member(is_joined[a].group)
            elif not is_joined[a] and is_joined[b]:
                cnt -= 1
                is_joined[a] = Member(is_joined[b].group)
            # 둘 다 그룹이 있는 경우, 두 그룹을 연결시켜줌
            # 이 경우, 한 그룹이 되기 때문에 카운트에서는 빼줘야 함
            else:
                # 그룹이 같은 경우, 아무 작업을 수행하지 않음
                if is_joined[a].group == is_joined[b].group:
                    continue
                cnt -= 1
                
        print(f"#{tc} {cnt}")

# git commit -m "code: Solve swea L5248 그룹 나누기 (yoonbaek)"