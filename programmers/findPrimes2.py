# 코딩테스트 연습 - 연습문제 - 소수 찾기
def solution(n):
    answer = 0

    #n = 1000 n까지의 소수 개수 구하기
    #에라토스테네스의 체 소수 구하기
    a = [False,False] + [True]*(n-1)
    primes = []

    for i in range(2,n+1):
        if a[i]:
            primes.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False
    
    answer = len(primes)
    
    
    return answer
