# 월간 코드 챌린지 시즌2 - 약수의 개수와 덧셈
def solution(left, right):
    answer = 0
    
    for i in range(left, (right+1)):
        if(NumberOfDivisor(i) % 2 == 0) :
            answer += i
        else : 
            answer -= i
    
    return answer

def NumberOfDivisor(n):

    divisors = []

    for i in range(1, int(n**(1/2)) + 1) :
        if(n % i == 0) :
            divisors.append(i)
            if((i**2) != n) :
                divisors.append(n // i)
    #divisors.sort()
    return len(divisors)



# 제곱수는 약수의 개수가 홀수. A==B 가 같아 짝지어 지지 않기 때문에 (다른 사람 풀이)
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5: # 제곱수는 홀수
            answer -= i
        else: # 제곱수가 아닌 것은 짝수
            answer += i
    return answer
