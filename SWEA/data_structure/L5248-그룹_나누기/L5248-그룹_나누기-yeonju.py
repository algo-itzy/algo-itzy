# 딱 테스트 케이스만 통과가 되었는데, 뭐가 문제인지 아직도 못 찾았습니다,,ㅠㅜ  

# 어떤 숫자가 기존의 그룹에 들어있으면, cnt 안 하고 그 둘을 붙임 = 같은 조로 묶어버림
# 없으면 리스트에 추가 조 만들어줌
# for 문 돌면서 그룹 내에 없는 애들, cnt 에 추가하고 최종 값 출력

for tc in range(int(input())):
    n, m = map(int, input().split())
    li = list(map(int, input().split()))

    group_gathered = [[li[0], li[1]]]
    cnt = 1                     # 그룹의 개수 카운트

    for i in range(2, len(li), 2):
        for j in range(0, len(group_gathered)):
            if li[i] in group_gathered[j] or li[i+1] in group_gathered[j]:
                group_gathered[j].append(li[i])
                group_gathered[j].append(li[i+1])
                break           # group_gathered[i] 안에 하나라도 있으면 for 문 나가기
        else:
            cnt += 1
            group_gathered.append([li[i], li[i+1]])

    for i in range(1, n+1):
        for j in range(len(group_gathered)):
            if i in group_gathered[j]:
                break
        else:
            cnt += 1

    print(f'#{tc+1} {cnt}')



# git commit -m "code: Solve swea L5248 그룹 나누기 (yeonju)"