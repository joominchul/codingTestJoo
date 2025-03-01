#https://school.programmers.co.kr/learn/courses/30/lessons/17680#
from collections import deque 
def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    if cacheSize == 0:                  #캐시 사이즈가 0일 때
        return len(cities) * 5
    for city in cities:
        city = city.upper()
        if city not in cache:           #캐시에 도시 없을 때
            if len(cache) >= cacheSize: #캐시에 공간 없으면 오래된 거 뺌
                cache.popleft()
            cache.append(city)
            answer += 5
        else:                           #캐시에 도시가 있을 때
            cache.remove(city)
            cache.append(city)
            answer += 1
                
    return answer
