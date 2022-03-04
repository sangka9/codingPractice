코딩테스트 연습 - 2022 KAKAO BLIND RECRUITMENT - 신고 결과 받기
def solution(id_list, report, k):
    answer = [0 for i in range(len(id_list))]
    fromList = [[] for i in range(len(id_list))]
    report = list(set(report))
    
    for i in report :
        toFrom = i.split()
        fromList[id_list.index(toFrom[1])].append(toFrom[0])
        
    for i in range(len(fromList)) :
        if len(fromList[i]) >= k :
            for j in fromList[i] :
                answer[id_list.index(j)] += 1
    
    return answer
