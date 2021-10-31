def solution(cacheSize, cities):

    time = 0
    cache_list = []             # 캐시에 저장될 도시를 담아둘 리스트 생성
    for city in cities:
        city = city.lower()     # 주의: 조건에서 대소문자 구분 없다고 했음
        if city in cache_list:  # 캐시에 해당 도시가 이미 들어있던 경우
            time += 1
            cache_list.pop(cache_list.index(city))
            cache_list.append(city)
        else:                   # 캐시에 해당 도시가 들어있지 않은 경우
            time += 5
            if cacheSize > 0:   # 주의: pop(0)은 캐시 리스트의 길이가 0인 경우 못하기에 경우를 또 나눔
                if len(cache_list) < cacheSize: # 캐시 리스트에 여유 공간이 있는 경우
                    cache_list.append(city)
                else:           # 캐시 리스트가 꽉 차있는 경우
                    cache_list.pop(0)
                    cache_list.append(city)
            else:               # 캐시 리스트 길이가 0인 경우
                pass
    return time


print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))

# git commit -m "code: Solve programmers 캐시 (yeonju)"