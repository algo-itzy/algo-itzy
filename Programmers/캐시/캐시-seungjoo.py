# git commit -m "code: Solve programmers 캐시 (seungjoo)"
def solution(cacheSize, cities):
    cache = []
    total_cost = 0
    for city in cities:
        lo_city = city.lower()
        if lo_city not in cache:
            cache.append(lo_city)
            total_cost += 5
            if len(cache) > cacheSize:
                cache.pop(0)
        else:
            cache.append(cache.pop(cache.index(lo_city)))
            total_cost += 1
    return total_cost