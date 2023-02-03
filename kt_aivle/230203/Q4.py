# Q4 Answer Template

def solution(arr):
    answer = LCM(arr[0],arr[1])
    
    for i in range(2,len(arr)) :
        answer = LCM(answer,arr[i])
        
    return answer

# 최대공약수 구하기
def GCD(x,y) :
    while y : #y가 참인 동안 = 자연수일때 = a%b != 0
        x,y = y, x%y
    return x
  
# 최소공배수 구하기
def LCM(a,b) :
    return (a*b)//GCD(a,b)

arr = [None]*15
arr = [2,6,8,14]
answer = solution(arr)
print(answer)
