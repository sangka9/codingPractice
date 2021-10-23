# CJ올리브네트웍스 2번문제
from itertools import combinations

def solution( x, y, a, b):
    answer = 0
    d = []

    for i in range(len(x)) :
        d.append([x[i],y[i]])

    combi = list(combinations(d,a))
    maxi = combiB(combi[0],d,b)
    d.clear()
    for i in range(len(x)) :
        d.append([x[i],y[i]])

    for i in range(len(combi)) :
        tmp =combiB(combi[i],d,b)
        if(maxi < tmp) :
            maxi = tmp
        d.clear()
        for i in range(len(x)) :
            d.append([x[i],y[i]])

    return maxi


def shortDistance(a1, b1, a2, b2) :
    x1,x2 = max(a1,a2), min(a1,a2)
    y1,y2 = max(b1,b2), min(b1,b2)

    res = (x1-x2) + (y1-y2)

    return res*res


def combiB(c,d,b) :
    for i in range(len(c)) :
        index = d.index(c[i])
        del d[index]

    l = list(combinations(d,b))

    #print(c)
    miniC = shortDistance(c[0][0],c[0][1],c[1][0],c[1][1])

    for i in range(len(c)) :
        for j in range(i+1,len(c)) :
            tmp =  shortDistance(c[i][0],c[i][1],c[j][0],c[j][1])
            print(tmp)
            if(tmp < miniC) :
                miniC = tmp

    miniL = shortDistance(l[0][0][0],l[0][0][1],l[0][1][0],l[0][1][1])

    for i in range(len(l)) :
        for j in range(i+1,len(l)):
            tmp = shortDistance(l[i][0][0],l[i][0][1],l[j][0][0],l[j][0][1])
            if(tmp < miniL) :
                miniL = tmp

    return min(miniL,miniC)
