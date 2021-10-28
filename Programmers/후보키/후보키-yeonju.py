# (0,1,2) 는 (0,1) 이 있으면 정답으로 추가시키지 않는 것을 아직 못해서,, 완성되지 못한 코드입니다 ㅠㅠ


from itertools import combinations


def solution(relation):
    answer = 0

    category = len(relation[0])
    num = len(relation)
    comb = []

    for i in range(1, category + 1):
        comb.extend(combinations(range(category), i))

    for i in comb:
        li = []
        print('아이', i)
        for k in range(num):
            tmp = []
            for j in i:
                # print('케이제이', relation[k][j])
                tmp.append(relation[k][j])

            li.append(tmp)
            print()
        print(li)
        b = list(map(tuple,li))
        c = set(b)
        print(c)


    return answer


solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]])


# git commit -m "code: Solve programmers 후보키 (yeonju)"