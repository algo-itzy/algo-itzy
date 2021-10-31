from collections import deque

class Cache(deque):
    def __init__(self, size):
        self.size = size

    def isfull(self):
        return len(self) >= self.size


def solution(cacheSize, cities):
    cache = Cache(size=cacheSize)
    eta = 0
    
    if cacheSize == 0:
        return len(cities) * 5
    
    for city in cities:
        city = city.lower()
        if city in cache:
            eta += 1
            cache.remove(city)
        else:
            eta += 5
            if cache.isfull():
                cache.popleft()
                
        cache.append(city)

    return eta


# git commit -m "code: Solve programmers 캐시 (yoonbaek)"