#SK ICT 1번 문제
def solution(money, costs):
    answer = 0

    minCost1 = costs[0]
    minCost5 = min([costs[0]*5,costs[1]])
    minCost10 = min([costs[0]*10,costs[1]*2,costs[2]])
    minCost50 = min([costs[0]*50,costs[1]*10,costs[2]*5,costs[3]])
    minCost100 = min([costs[0]*100,costs[1]*20,costs[2]*10,costs[3]*2,costs[4]])
    minCost500 = min([costs[0]*500,costs[1]*100,costs[2]*50,costs[3]*100,costs[4]*5,costs[5]])

    while (1) :
        if money == 0:
            break
        else :
            if money >= 500 :
                answer += (money // 500) * minCost500
                money %= 500
            elif money >= 100 :
                answer += (money // 100) * minCost100
                money %= 100
            elif money >= 50 :
                answer += (money // 50) * minCost50
                money %= 50
            elif money >= 10 :
                answer += (money // 10) * minCost10
                money %= 10
            elif money >= 5 :
                answer += (money // 5) * minCost5
                money %= 5
            elif money >= 1 :
                answer += (money // 1) * minCost1
                money %= 1

    return answer
