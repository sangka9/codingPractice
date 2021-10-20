# 2021 KAKAO BLIND RECRUITMENT - 메뉴 리뉴얼
from itertools import combinations

def solution(orders, course):
    answer = []
    res = [[] for i in range(course[len(course)-1]+1)]
    
    for i in range(len(orders)) :
        for j in range(len(course)) :
            tmp = list(orders[i])
            tmp.sort()
            orders[i] = ''.join(tmp)
            if(len(orders[i]) > course[j]) :
                tmp = list(map(''.join, combinations(orders[i], course[j])))
                res[course[j]] = res[course[j]] + tmp
            elif(len(orders[i]) == course[j]) :
                tmp = [orders[i]]
                res[course[j]] = res[course[j]] + tmp
    
    for i in range(len(res)) :
        if(len(res[i]) > 0) :
            res[i].sort()
            tmp = couting(res[i])
            answer += tmp
    answer.sort()
    
    return answer

def couting(menu):
    course = []
    tmp = []
    
    for i in range(len(menu)) :
        if(menu.count(menu[i]) > 1) :
            if(len(tmp) == 0) :
                tmp.append([menu[i], menu.count(menu[i])])
            elif(menu.count(menu[i]) > tmp[0][1]) :
                tmp.clear()
                tmp.append([menu[i], menu.count(menu[i])])
            elif(menu.count(menu[i]) == tmp[0][1]) :
                for j in range(len(tmp)) :
                    if(menu[i] == tmp[j][0]) :
                        break
                else :
                    tmp.append([menu[i], menu.count(menu[i])])
    
    for i in range(len(tmp)) :
        course.append(tmp[i][0])
    
    return course
