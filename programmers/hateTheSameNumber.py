#코딩테스트 연습 - 연습문제 - 같은 숫자는 싫어
def solution(arr):
    answer = []

    for i in range(0,len(arr)-1) :
        if arr[i] != arr[i+1] :
            answer.append(arr[i])
    answer.append(arr[-1])
    
    return answer
