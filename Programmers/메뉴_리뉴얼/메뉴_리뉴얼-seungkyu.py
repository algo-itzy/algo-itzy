# git commit -m "code: Solve programmers 메뉴 리뉴얼 (seungkyu)"
from itertools import combinations


def make_comb(orders, num):
    comb = set()
    for order in orders:
        for item in combinations(list(order), num):
            comb.add(item)
    return comb


def find_course(orders, comb):
    comb_cnt = [comb , 0]  # [(조합), 조합수 저장]
            
    for order in orders:
        flag = False
        for item in comb_cnt[0]:  # cnt[0] : 조합
            if item not in order:
                flag = False  # 조합 없으면 break
                break
            flag = True
        if flag:  # 조합 있으면 조합수+1
            comb_cnt[1] += 1 

    return comb_cnt

def solution(orders, course):
    answer = set()

    for num in course:
        answer_list = []  # 조합 후보 모두 저장, 몇 명이 골랐는지는 나중에 고려
        combination = make_comb(orders, num)  # 조합 생성

        for comb in combination:
            comb_cnt = find_course(orders, comb)  # 조합 만들 수 있는지 체크
            
            if comb_cnt[1] >= 2:  # 조합수 2개 이상이어야 함
                answer_list.append(comb_cnt)
                
        if answer_list:  # 길이에 맞는 후보코스가 1개라도 있는 경우
            # 조합수 많은 순 정렬, 제일 앞의 값이 최대
            answer_list = sorted(answer_list, key = lambda x: -x[1])  
            max_num = answer_list[0][1]
            
            for comb in answer_list:
                if comb[1] == max_num:  # 조합 최대값 여러 개일 가능성 고려
                    ans = sorted(list(comb[0]))  # 답에서 XY, YX 2개 나오지 않도록 정렬
                    answer.add(''.join(ans))
                
    answer = list(answer)
    answer.sort()
    return answer
