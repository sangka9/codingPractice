# Summer/Winter Coding(2019) - 멀쩡한 사각형 * 수학적 패턴을 알아내기 어려웠던 문제

import math

def solution(w,h):
    answer = 1
    
    answer = (w * h) - (w + h - math.gcd(w,h))
    
    return answer
