from itertools import combinations

def solution(info, query):
    answer = []
    dic = {}
    
    for x in info:
        x = x.split()
        spec, score = x[:-1], int(x[-1]) 

        for n in range(5):
            cases = list(combinations(range(4), n))

            for case in cases:
                tmp = spec.copy()

                for i in case:
                    tmp[i] = '-'
                
                tmp = ''.join(tmp)

                if tmp in dic:
                    dic[tmp].append(score)
                else:
                    dic[tmp] = [score]

    for value in dic.values():  # 이분탐색 위해 value 정렬
        value.sort()

    for q in query:
        q = [i for i in q.split() if i != 'and']

        tmp, score = ''.join(q[:-1]), int(q[-1])
        
        if tmp in dic:
            data = dic[tmp]

            if data:          
                s, e = 0, len(data)-1  # 중복 배열에서 가장 앞 인덱스 탐색

                while s <= e:
                    m = (s+e) // 2

                    if data[m] < score:
                        s = m+1
                    else:
                        e = m-1

                answer.append(len(data) - s)
        else:
            answer.append(0)

    return answer