#SK ICT 2차 1번 문제
from itertools import combinations
def solution(goods):
    answer = []

    for i in range(len(goods)) :
        items = list(goods[i]) # 문자 선정
        onlyOne = [] # 고유검색어 목록

        for j in range(1, len(items)): # 문자 조합
            combi = list(map(''.join, combinations(items, j)))

            for k in range(len(combi)) :
                matchList = list(filter(lambda x: combi[k] in x, goods))
                if len(matchList) == 1 and goods[i] in matchList : # 고유검색어인 경우
                    onlyOne.append(combi[k])

            if len(onlyOne) > 0 :
                onlyOne = list(set(onlyOne)) # 중복제거
                onlyOne.sort() # 정렬
                answer.append(" ".join(onlyOne)) #문자열 합친 후 정답에 추가
                break


        if len(onlyOne) == 0 :
            answer.append("None")


    return answer
