# 코딩테스트 연습 - 해시 - 완주하지 못한 선수
from collections import Counter

def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    
    return list(answer.keys())[0]
