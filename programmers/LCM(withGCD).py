#코딩테스트 연습 - 연습문제 - N개의 최소공배수
import math
def solution(arr):
    answer = 1
    
    for i in arr :
        answer = (answer*i)//math.gcd(answer,i)
    
    return answer
  
  
#유클리드 호제법
#최대공약수 구하기
def GCD(x,y) :
    while y : #y가 참인 동안 = 자연수일때 = a%b != 0
        x,y = y, x%y
    return x
  
#최소공배수 구하기
def LCM(a,b) :
    return (a*b)//GCD(a,b)
