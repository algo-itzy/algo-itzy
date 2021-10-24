# git commit -m "code: Solve programmers 순위 검색 (jiwoong)"
# 효율성 실패
def solution(info, query):
    ans = [0 for x in range(len(query))]
    q_list = []
    i_list = []
    # 쿼리
    for i in range(len(query)):
        test = query[i].split()
        while 'and' in test:
            test.remove('and')
        q_list.append(test)

    # info
    for j in info:
        t = j.split()
        i_list.append(t)

    # 비교
    for i in range(len(i_list)):
        for j in range(len(q_list)):
            flag = 0
            for k in range(4):
                if i_list[i][k] != q_list[j][k]:
                    if q_list[j][k] != '-':
                        flag = 1
                        break
            if flag == 0:
                if int(i_list[i][4]) >= int(q_list[j][4]):
                    ans[j] += 1
    return ans
