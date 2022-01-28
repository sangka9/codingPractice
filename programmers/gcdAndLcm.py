# 코딩테스트 연습 - 연습문제 - 최대공약수와 최소공배수
def solution(n, m):
    answer = []
    
    answer.append(gcd(n,m))
    answer.append(lcm(n,m))
    
    return answer


def gcd(x,y) :
    while y :
        x, y = y, x%y
    return x

def lcm(x,y) :
    return (x*y)//gcd(x,y)
