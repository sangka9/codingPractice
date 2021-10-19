# 2018 KAKAO BLIND RECRUITMENT - [1차] 캐시
def solution(cacheSize, cities):
    answer = 0
    cache = []
        
    for i in range(len(cities)) :
        cities[i] = cities[i].lower()
        
        if(cacheSize == 0) : # cacheSize가 0 인 경우
            answer = len(cities) * 5
            break
        
        if (cities[i] in cache) : # hit
            recent = cache.index(cities[i])
            cache = [cache[recent]] + cache[:recent] + cache[recent+1:]
            answer += 1
        else : # miss
            if(len(cache) == cacheSize) :
                cache.pop(-1)
            cache = [cities[i]] + cache
            answer += 5

    return answer
