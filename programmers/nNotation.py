# 2018 KAKAO BLIND RECRUITMENT - [3차] n진수 게임
def solution(n, t, m, p):
    answer = ''
    alphaNumber = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
    endNumbersLength = m * t
    count = 0
    numbers = ''
    
    while(1) : # 길이보다 최소로 크게 진법 변환해서 numbers에 넣기
        numbers = numbers + nNotation(count,n,alphaNumber)
        if(len(numbers) > endNumbersLength) :
            break
        count += 1
        
    for i in range(endNumbersLength) :
        if (i % m) == (p - 1) :
            answer = answer + numbers[i]        
    
    return answer

def nNotation (number, n, aN) :
    ans = ''
    while(1) :
        if(number >= n) :
            if(number % n > 9) :
                ans = aN[number % n] + ans
            else :
                ans = str(number % n) + ans
            number = number // n
        else :
            if(number % n > 9) :
                ans = aN[number] + ans
            else :
                ans = str(number) + ans
            break
    return ans
