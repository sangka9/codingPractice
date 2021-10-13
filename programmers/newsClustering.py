# 2018 KAKAO BLIND RECRUITMENT - [1차] 뉴스 클러스터링
def solution(str1, str2):
    answer = 0 
    twoWord1 = []
    twoWord2 = []
    
    for i in range(len(str1)-1) :
        if(str1[i:i+2].lower()).isalpha() :
            twoWord1.append(str1[i:i+2].lower())
        
    for i in range(len(str2)-1) :
        if(str2[i:i+2].lower()).isalpha() :
            twoWord2.append(str2[i:i+2].lower())
    
    duTwoWord1 = []
    duTwoWord2 = []
    
    for i in range(len(twoWord1)) :
        if(twoWord1.count(twoWord1[i]) > 1) :
            duTwoWord1.append(twoWord1[i])
    
    for i in range(len(twoWord2)) :
        if(twoWord2.count(twoWord2[i]) > 1) :
            duTwoWord2.append(twoWord2[i])
    
    duTwoWord1 = list(set(duTwoWord1))
    duTwoWord2 = list(set(duTwoWord2))
            
    if (len(twoWord1) + len(twoWord2)) == 0 :
        return 65536
    else :
        intersectionSet = list(set(twoWord1).intersection(twoWord2))
        mini = 0
        for i in range(len(intersectionSet)) : # 교집합    
            if(intersectionSet[i] in duTwoWord1)or(intersectionSet[i] in duTwoWord2) :
                a = twoWord1.count(intersectionSet[i])
                b = twoWord2.count(intersectionSet[i])
                mini += min(a,b) - 1
        
        unionSet = list(set(twoWord1).union(twoWord2))
        maxi = 0
        for i in range(len(unionSet)) : # 합집합
            if(unionSet[i] in duTwoWord1) or (unionSet[i] in duTwoWord2) :
                a = twoWord1.count(unionSet[i])
                b = twoWord2.count(unionSet[i])
                maxi += max(a,b) - 1

        answer = (len(intersectionSet) + mini) / (len(unionSet) + maxi)
        answer = int(answer * 65536)
    
    return answer
