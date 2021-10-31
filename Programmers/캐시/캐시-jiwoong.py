# git commit -m "code: Solve programmers 캐시 (jiwoong)"
def solution(cacheSize, cities):
    cities = map(lambda x: x.lower(), cities)
    arr = []
    answer = 0
    for i in cities:
        if i in arr:
            answer += 1
            arr.pop(arr.index(i))
            arr.append(i)
        else:
            answer += 5
            arr.append(i)
        if len(arr) > cacheSize:
            arr.pop(0)
    return answer
