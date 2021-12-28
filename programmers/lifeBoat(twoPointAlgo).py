# 코딩테스트 연습 - 탐욕법(Greedy) - 구명보트
def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    front = 0
    back = len(people)-1

    while front <= back :
        if people[front] + people[back] <= limit :
            back -= 1
        front += 1
        answer += 1
    
    return answer
