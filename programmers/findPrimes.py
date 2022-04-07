# 코딩테스트 연습 - 완전탐색 - 소수 찾기
from itertools import permutations
def solution(numbers):
    answer = 0
    
    strN = list(str(numbers))
    strN.sort(reverse = True)
    primes = int(''.join(strN)) + 1
    primes = getPrimes(primes)
    
    print(len(strN))
    for i in range(1,len(strN)+1) :
        permuN = list(permutations(strN, i))
        permuN = list(set(permuN))
        
        for i in range(len(permuN)) :
            n = ''.join(permuN[i])
            if int(n) in primes :
                answer += 1
                primes.remove(int(n))
            
    return answer

def getPrimes(n):
    # n = 3000
    a = [False,False] + [True]*(n-1)
    primes = []

    for i in range(2,n+1):
        if a[i]:
            primes.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False
            
    return primes
