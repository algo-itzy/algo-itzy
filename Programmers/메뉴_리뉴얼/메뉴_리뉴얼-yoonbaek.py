from itertools import combinations

def sort_order(order):
    sorted_order = ''

    cnt_sort_memo = [0] * 26
    for char in order:
        cnt_sort_memo[ord(char)-65] += 1
        
    for i in range(26):
        if cnt_sort_memo[i]:
            sorted_order += chr(i+65)

    return sorted_order


def solution(orders, courses):
    set_menus = []
    menu_cnt = {}
    
    for order in orders:
        order = sort_order(order)
        N = len(orders)
        for r in range(2, N+1):
            combies = combinations(order, r)

            for c in combies:
                if c not in menu_cnt:
                    menu_cnt[c] = 1
                else:
                    menu_cnt[c] += 1

    for num in courses:
        cur_max = 0
        course = []
        for key in menu_cnt:
            if len(key) == num:
                if menu_cnt[key] != 1 and menu_cnt[key] > cur_max:
                    course = [key]
                    cur_max = menu_cnt[key]
                elif menu_cnt[key] == cur_max:
                    course.append(key)
        
        for c in course:
            set_menus.append(c)

    answer = []
    for set_menu in set_menus:
        s = ''
        for menus in set_menu:
            s += menus
        answer.append(s)

    answer.sort()    
    return answer

orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
print(solution(orders, [2, 3, 5]))
# git commit -m "code: Solve programmers 메뉴 리뉴얼 (yoonbaek)"