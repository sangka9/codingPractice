# Q5 Answer template
def solution(n, s):
    answer = []
    
    if s == 1:
        return -1
    
    m = (s-1)*1
    
    for i in range(1,s//2+1) :
        if (s-i) * i > m :
            m = (s-i) * i
            answer = [i,s-i]
    
    return answer

n = 2
s = 9
answer = solution(n, s)
print(answer)
