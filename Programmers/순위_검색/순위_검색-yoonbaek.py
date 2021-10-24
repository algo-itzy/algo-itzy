import heapq

applicant_dict = {
    0: ("cpp", "java", "python"),
    1: ("backend", "frontend"),
    2: ("junior", "senior"),
    3: ("chicken", "pizza"),
}

keys = []

def backtrack(key, i, combs):
    global keys
    if i == 4:
        keys.append(tuple(combs))
        return

    if key[i] == '-':
        for val in applicant_dict[i]:
            backtrack(key, i+1, combs + [val])
    else:
        backtrack(key, i+1, combs + [key[i]])


def binary_search(criteria, values):
    start, end = 0, len(values)

    while start < end:
        mid = (start + end) // 2
        if values[mid] >= criteria:
            end = mid
        else:
            start = mid+1
    
    return len(values) - start


def solution(infos, queries):
    global keys
    applicants = {}

    for info in infos:
        info = info.split()
        key = tuple(info[:-1])
        val = int(info[-1])
        if key not in applicants:
            applicants[key] = [val]
        else:
            heapq.heappush(applicants[key], val)

    answer = []

    for query in queries:
        query = query.replace("and", "").split()
        key = query[:-1]

        keys = []
        backtrack(key, 0, []) # keys 배열 구하기

        criteria = int(query[-1])
        
        cnt = 0
        for key in keys:
            if key in applicants:
                cnt = binary_search(criteria, applicants[key])
                    
        answer.append(cnt)

    return answer

if __name__ == "__main__":
    info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
    query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
    print(solution(info, query))

# git commit -m "code: Solve programmers 순위 검색 (yoonbaek)"