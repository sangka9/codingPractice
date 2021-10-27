#Summer/Winter Coding(~2018) - 영어 끝말잇기
def solution(n, words):
    answer = []
    who = 0
    num = 0
    overlap = [words[0]]
    
    for i in range(1,len(words)) :
        last = words[i-1][-1]
        if(words[i][0] != last) or (words[i] in overlap) :
            who = i % n + 1
            num = i // n + 1
            break
        overlap.append(words[i])
        
    answer.append(who)
    answer.append(num)
    
    return answer
