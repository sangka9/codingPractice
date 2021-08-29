# 2021 카카오 채용연계형 인턴십 - 숫자 문자열과 영단어
def solution(s):
    answer = 0
    
    numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        
    for i in range(10) :
        s = s.replace(numbers[i], f'{i}')

    answer = int(s)
    
    return answer
