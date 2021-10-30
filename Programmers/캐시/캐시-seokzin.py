from collections import deque


def solution(cacheSize, cities):
    answer = 0
    cache = deque()

    if cacheSize == 0: 
        return len(cities) * 5
    else: 
        for c in cities: 
            c = c.lower()

            if c in cache:
                cache.remove(c)
                cache.append(c)
                answer += 1
            else: 
                if len(cache) < cacheSize:
                    cache.append(c)
                else:
                    cache.popleft()
                    cache.append(c)
                answer += 5

    return answer