# 코딩테스트 연습 - 연습문제 - 최댓값과 최솟값
def solution(s):
    answer = ''
    
    t = s.split()
    t = list(map(int, t))
    t.sort()
    
    answer += str(t[0]) + " " + str(t[-1])
    # answer += f'{min(t)} {max(t)}'
    
    return answer
