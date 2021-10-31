# git commit -m "code: Solve programmers 캐시 (seungkyu)"
from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    
    if cacheSize == 0:
        answer = 5*len(cities)
    else:
        for city in cities:
            city = city.lower()
            if len(cache) == 0:
                cache.append(city)
                answer += 5
            else:
                if city in cache:
                    cache.remove(city)
                    cache.append(city)
                    answer += 1
                else:
                    if len(cache) < cacheSize:
                        cache.append(city)
                    else:
                        cache.popleft()
                        cache.append(city)
                    answer += 5
    
    return answer