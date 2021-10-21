from itertools import combinations


def solution(orders, course):
    answer = []
    for c in course:        # 2개짜리, 3개짜리 메뉴의 조합 구함
        menus = dict()
        tmp = list()
        for order in orders:
            li = list(combinations(sorted(order), c))
            tmp.extend(li)

        for t in tmp:       # 조합에 해당되는 개수만큼 딕셔너리에 담음
            key = ''.join(t)

            if key in menus:
                menus[key] += 1
            else:
                menus[key] = 1

        for menu in menus:
            if max(menus.values()) > 1: # 단품 메뉴 2개 이상
                if menus[menu] == max(menus.values()): # 가장 많이 함께 주문된 메뉴 구성이면 answer 에 추가
                    answer.append(menu)


    answer.sort()                       # 오름차순 정렬

    return answer



# git commit -m "code: Solve programmers 메뉴 리뉴얼 (yeonju)"