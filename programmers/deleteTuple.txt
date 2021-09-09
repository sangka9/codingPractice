# 2017 팁스타운 - 짝지어 제거하기
def solution(s):
    answer = 1
    st = []
    
    for i in s:
        if(len(st) > 0) and st[-1] == i:
            st.pop()
        else:
            st.append(i)
        
    if(len(st) == 0):
        answer = 1
    else :
        answer = 0
        
    return answer
