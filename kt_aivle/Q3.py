# Q3 Answer template

def solution(left, right):
    answer = 0
    
    for i in range(left,right+1) :
        if len(getMyDivisor(i))% 2 == 0 : # 약수의 개수가 짝수인 경우
            answer += i
        else : # 약수의 개수가 홀수인 경우
            answer -= i
            
    return answer

def getMyDivisor(n): 
    divisorsList = [] # 약수의 개수 리스트

    print(n, int(n**(1/2)) + 1)
    for i in range(1, int(n**(1/2)) + 1):
        if (n % i == 0):
            divisorsList.append(i) 
            if ( (i**2) != n) : # 25 = 5*5 와 같은 A==B인 경우 제외
                divisorsList.append(n // i)

    #divisorsList.sort()
    #print(divisorsList)
    
    return divisorsList

left = 13
right = 17
c = solution(left, right)
print(c)
